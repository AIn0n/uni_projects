#!/usr/bin/env python3
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def hello():
    params = request.args.to_dict()
    if "num1" in params and "num2" in params:
        a = int(params["num1"])
        b = int(params["num2"])
        return json.dumps({"sum": a + b, "sub": a - b, "div": a // b, "mod": a % b})
    return "no str parameter found"
