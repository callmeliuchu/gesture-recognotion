import json
import threading

from flask import Flask
from flask import request
import requests

import serversocket
import serversocket as sr

app = Flask(__name__)

prefix = "http://"

host = "http://127.0.0.1:5032"

errObject = {
    "code": 500,
}


def start_web():
    app.run('127.0.0.1', port=8080, debug=True)


@app.route('/start_socket', methods=['GET'])
def start_socket():
    serversocket.start_socket()
    success = {
        "code": 200,
    }
    return json.dumps(success)


# 接收客户端请求，调用预测服务，返回结果
@app.route('/command', methods=['POST'])
def command():
    body = request.json
    requestBody = {
        'image': body['image']
    }
    try:
        res = requests.post(url=host + '/paddle/predict',
                            headers={"Content-Type": "application/json; charset=utf-8"},
                            data=json.dumps(requestBody))
    except:
        return json.dumps(errObject)
    res = res.json()
    status = res["success"]
    if not status:
        return json.dumps(errObject)
    predict = res["predict"]
    success = {
        "code": 200,
        "data": {
            "predict": predict
        }
    }
    serversocket.send(predict)
    return json.dumps(success)


if __name__ == '__main__':
    start_web()
