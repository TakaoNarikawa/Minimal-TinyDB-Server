from flask import Flask, request, jsonify
import logging
import argparse

import param_rule
import utils

app = Flask(__name__)

# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(stream_handler)
file_handler = logging.FileHandler("server.log", mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(file_handler)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/get-doc', methods=['GET'])
def get_doc():
    params = request.json
    if not param_rule.get_validator.validate(params):
        return jsonify({"message": f'エラー,無効なパラメータ "{param_rule.get_validator.errors}"'}), 400

    table = params.get("table", None)
    index = params.get("index", None)
    from_i = params.get("from_i", None)
    to_i = params.get("to_i", None)

    db = utils.select_table(table)
    data = db.all()

    if index != None:
        return jsonify({"data": utils.get_at(data, index, None)})

    if from_i != None or to_i != None:
        from_i = from_i or 0
        to_i = to_i or len(data)
        return jsonify({"data": data[from_i:to_i]})

    return jsonify({"data": data})

@app.route('/add-doc', methods=['POST'])
def add_doc():
    params = request.json
    if not param_rule.add_validator.validate(params):
        return jsonify({"message": f'エラー,無効なパラメータ "{param_rule.add_validator.errors}"'}), 400

    table = params.get("table", None)
    value = params.get("value", None)

    db = utils.select_table(table)
    db.insert(value)

    return jsonify({"message": "成功"})

@app.route('/update-doc', methods=['POST'])
def update_doc():
    params = request.json
    if not param_rule.update_validator.validate(params):
        return jsonify({"message": f'エラー,無効なパラメータ "{param_rule.update_validator.errors}"'}), 400

    table = params.get("table", None)
    index = params.get("index", None)
    value = params.get("value", None)

    db = utils.select_table(table)
    doc = utils.get_at(db.all(), index, None)
    if doc != None:
        db.update(value, doc_ids=[doc.doc_id])
        return jsonify({"message": "成功"})
    else:
        return jsonify({"message": "指定されたindexにマッチするものが見つかりませんでした"})


@app.route('/delete-doc', methods=['POST'])
def delete_doc():
    params = request.json
    if not param_rule.delete_validator.validate(params):
        return jsonify({"message": f'エラー,無効なパラメータ "{param_rule.delete_validator.errors}"'}), 400

    table = params.get("table", None)
    index = params.get("index", None)

    db = utils.select_table(table)
    doc = utils.get_at(db.all(), index, None)
    if doc != None:
        db.remove(doc_ids=[doc.doc_id])
        return jsonify({"message": "成功"})
    else:
        return jsonify({"message": "指定されたindexにマッチするものが見つかりませんでした"})

@app.route('/delete-table', methods=['POST'])
def delete_table():
    params = request.json
    if not param_rule.delete_table_validator.validate(params):
        return jsonify({"message": f'エラー,無効なパラメータ "{param_rule.delete_table_validator.errors}"'}), 400

    table = params.get("table", None)

    db = utils.select_table(table)
    db.remove(doc_ids=[doc.doc_id for doc in db.all()])

    return jsonify({"message": f"成功:{table}の内容をリセットしました"})

@app.route('/delete-all', methods=['POST'])
def delete_all():
    _db = utils.get_db()
    for table in _db.tables():
        db = utils.select_table(table)
        db.remove(doc_ids=[doc.doc_id for doc in db.all()])

    return jsonify({"message": "すべてのデータがリセットされました"})

def main(args):
    host, port = args.host, args.port
    app.run(host=host, port=port)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default=utils.LOCAL_IP_ADDR)
    parser.add_argument('--port', type=int, default=8080)
    args = parser.parse_args()

    main(args)
