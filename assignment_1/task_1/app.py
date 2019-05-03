from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/task_1')
def server(methods=["POST"]):
    # might be request.args.get('a')
    a = int(request.form['a'])
    b = int(request.form['b'])
    # a = int(request.args.get('a'))
    # b = int(request.args.get('b'))
    return str(solve(a, b))

def solve(a, b):
    return a + b