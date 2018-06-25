# Flask restful Api 範例
## 環境安裝
* 安裝套件
```
pip install -r requirement.txt
```
* 設定全域指令
```
# For Linux and Mac:
export FLASK_APP=flaskr
export FLASK_ENV=development
```
```
# For Windows cmd, use set instead of export:
set FLASK_APP=flaskr
set FLASK_ENV=development
```

## 初始化 DB
本篇使用 sqlite3
* 建立 schema，請修改 flask_restful_sample/flaskr/schema.sql
* 執行初始化
```
flask init-db
```
* 執行成功會看見 flask_restful_sample\instance\flaskr.sqlite

## Router 
* 在 flask_restful_sample/flaskr/url.py 中設定

## 執行
```
flask run
```
* http://127.0.0.1:5000/api/welcome