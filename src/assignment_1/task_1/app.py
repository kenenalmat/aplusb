from flask import Flask
from flask import request, Response, jsonify

app = Flask(__name__)

@app.route('/', methods=["POST"])
def server():
    # might be request.args.get('a')
    a = int(request.form['a'])
    b = int(request.form['b'])
    # a = int(request.args.get('a'))
    # b = int(request.args.get('b'))
    ans = {'result': solve(a, b)}
    print ("GOT THE RESULT: {}".format(ans['result']))
    return jsonify(ans)


def solve(a, b):
    return a + b
