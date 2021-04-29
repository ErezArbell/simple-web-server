#!/usr/bin/python3

import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/<string:text>', methods=['GET'])
def echo(text):
  return "<h3>You wrote:</h3>%s" % text, 200

@app.route("/ip", methods=["GET"])
def get_my_ip():
    return request.remote_addr, 200

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
