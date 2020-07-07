from flask import Flask, request
import logging
import argparse

from db import db
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
    params = request.args.to_dict()
    if not param_rule.get_validator.validate(params):
        return f"エラー:{param_rule.get_validator.errors}", 400

    params = [f"{name}: {message}" for name, message in params.items()]
    return '\n'.join(["あなたが入力したパラメータは次の通りです。"] + params)

@app.route('/add-doc', methods=['POST'])
def add_doc():
    params = request.json
    if not param_rule.add_validator.validate(params):
        return f"エラー:{param_rule.add_validator.errors}", 400

    params = [f"{name}: {message}" for name, message in params.items()]
    return '\n'.join(["あなたが入力したパラメータは次の通りです。"] + params)

@app.route('/update-doc', methods=['POST'])
def update_doc():
    params = request.json
    if not param_rule.update_validator.validate(params):
        return f"エラー:{param_rule.update_validator.errors}", 400

    params = [f"{name}: {message}" for name, message in params.items()]
    return '\n'.join(["あなたが入力したパラメータは次の通りです。"] + params)

@app.route('/delete-doc', methods=['POST'])
def delete_doc():
    params = request.json
    if not param_rule.delete_validator.validate(params):
        return f"エラー:{param_rule.delete_validator.errors}", 400

    params = [f"{name}: {message}" for name, message in params.items()]
    return '\n'.join(["あなたが入力したパラメータは次の通りです。"] + params)

@app.route('/delete-table', methods=['POST'])
def delete_table():
    params = request.json
    if not param_rule.delete_validator.validate(params):
        return f"エラー:{param_rule.delete_validator.errors}", 400

    params = [f"{name}: {message}" for name, message in params.items()]
    return '\n'.join(["あなたが入力したパラメータは次の通りです。"] + params)

@app.route('/delete-all', methods=['POST'])
def delete_all():
    params = request.json
    if not param_rule.delete_validator.validate(params):
        return f"エラー:{param_rule.delete_validator.errors}", 400

    params = [f"{name}: {message}" for name, message in params.items()]
    return '\n'.join(["あなたが入力したパラメータは次の通りです。"] + params)

def main(args):
    host, port = args.host, args.port
    app.run(host=host, port=port)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default=utils.LOCAL_IP_ADDR)
    parser.add_argument('--port', type=int, default=8080)
    args = parser.parse_args()

    main(args)
