# coding=utf-8
# 实现响应request请求，提取json数值

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def view():
    para1 = request.args.get('para1', '')
    para2 = request.args.get('para2', '')
    return_data = {'username': para1, 'passwd': para2}
    return json.dumps(return_data)


if __name__ == '__main__':
    app.run(debug=1, port=80)


