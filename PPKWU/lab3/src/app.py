#!/usr/bin/env python3
from flask import Flask, request
import json


app = Flask(__name__)

@app.route("/")
def hello():
    params = request.args.to_dict()
    if "str" in params:
        string = params["str"]
        return json.dumps({
            "lowercase": sum(map(str.islower, string)),
            "digits":    sum(map(str.isdigit, string)),
            "uppercase": sum(map(str.isupper, string)),
            "special": sum(not char.isalpha() and not char.isdigit() for char in string)
        })
    return "no str parameter found"
