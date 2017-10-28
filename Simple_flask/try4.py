# coding=utf-8
# 实现连接数据库,操作数据库返回给前端

from flask import Flask, render_template, request
import MySQLdb as mysql
import json

app = Flask(__name__)

# mysql默认端口3306
db = mysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='test', charset='utf8')
db.autocommit(True)
c = db.cursor()
# 详细可以参见python mysql教程


@app.route('/', methods=['GET', 'POST'])
def chart():
    c.execute("SELECT DATA FROM TEST")
    data = c.fetchall()
    return render_template('index.html', data=json.dumps(data))  # need creat json


if __name__ == '__main__':
    app.run(debug=1, port=80)
