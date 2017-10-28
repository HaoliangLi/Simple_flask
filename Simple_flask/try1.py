# coding=utf-8
# 实现url传参


from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def view1():
    return "hello world!"


@app.route('/<param>', methods=['GET', 'POST'])
def view2(param):
    return 'hello ' + param + '!!!'


if __name__ == '__main__':
    app.run(debug=1, port=80)



