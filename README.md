# Minimal-TinyDB-Server

NoSQL を用いた簡易的なデータベースサーバーを構築することができます。

シンプルであることに重きを置いたので、厳密な API サーバーのルールに従っていません。
GET と POST しか使用しておらず、エンドポイントも `/api/v1/xxx` の形にしていません。パラメータも全て JSON を用いて渡します。

# エンドポイント

```py
HOST = 'http://xxx.xxx.xxx.xxx:8080'
HEADERS = {'Content-Type': 'application/json'}
```

## **GET** `/get-doc`

データベースに保存されているデータを取得する

- `optional` table: 取得する対象のテーブル名、指定しないとデフォルトのテーブルが使用される
- `optional` index: テーブルの中から N 番目のデータを取得する場合指定する
- `optional` from_i: テーブルの中から N 番目以降のデータを取得する場合指定する
- `optional` to_i: テーブルの中から N 番目以前のデータを取得する場合指定する

```py
params = {
    'table': 'sample',
    'index': 3
}
response = requests.get(
    HOST + '/get-doc',
    data=json.dumps(params),
    headers=HEADERS)

response = json.loads(response.text)
print(response) # >> {'data': [{'foo': 'bar'}]}
```

## **POST** `/add-doc`

データベースに新たなデータを追加する

- `optional` table: 取得する対象のテーブル名、指定しないとデフォルトのテーブルが使用される
- `required` value: テーブルに追加する内容、辞書型で指定する

```py
params = {
    'table': 'sample',
    'value': {'foo': 'bar'}
}
response = requests.post(
    HOST + '/add-doc',
    data=json.dumps(params),
    headers=HEADERS)

response = json.loads(response.text)
print(response) # >> {'message': '成功'}
```

## **POST** `/update-doc`

データベースに含まれるデータの一部を更新する

- `optional` table: 取得する対象のテーブル名、指定しないとデフォルトのテーブルが使用される
- `required` value: 更新する内容、辞書型で指定する

```py
params = {
    'table': 'sample',
    'value': {'foo': 'bar'}
}
response = requests.post(
    HOST + '/update-doc',
    data=json.dumps(params),
    headers=HEADERS)

response = json.loads(response.text)
print(response) # >> {'message': '成功'}
```

## **POST** `/delete-doc`

データベースに含まれるデータを削除する

- `optional` table: 取得する対象のテーブル名、指定しないとデフォルトのテーブルが使用される
- `required` index: テーブルの中から N 番目のデータを取得する場合指定する

```py
params = {
    'table': 'sample',
    'index': 3
}
response = requests.post(
    HOST + '/delete-doc',
    data=json.dumps(params),
    headers=HEADERS)

response = json.loads(response.text)
print(response) # >> {'message': '成功'}
```

## **POST** `/delete-table`

データベースのテーブルを削除する

- `optional` table: 取得する対象のテーブル名、指定しないとデフォルトのテーブルが使用される

```py
params = {
    'table': 'sample',
}
response = requests.post(
    HOST + '/delete-table',
    data=json.dumps(params),
    headers=HEADERS)

response = json.loads(response.text)
print(response) # >> {'message': '成功:sampleの内容をリセットしました'}
```

## **POST** `/delete-all`

データベースに含まれるデータ全てを削除する

```py
response = requests.post(
    HOST + '/delete-all')

response = json.loads(response.text)
print(response) # >> {'message': 'すべてのデータがリセットされました'}
```
