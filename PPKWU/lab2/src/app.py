#!/usr/bin/env python3
from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/")
def hello():
    params = request.args.to_dict()
    if "cmd" in params and params["cmd"] == "time":
        return str(time.strftime("%H:%M:%S"))
    if "cmd" in params and "str" in params and params["cmd"] == "rev":
        return reversed(params["str"])
    return "Hello world!"
