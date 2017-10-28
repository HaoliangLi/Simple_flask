# coding=utf-8
# 实现hello world


from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def view():
    return "hello world!"


if __name__ == '__main__':
    app.run(debug=1, port=80)


