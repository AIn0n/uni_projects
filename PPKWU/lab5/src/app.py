#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    result = {}
    params = request.get_json()
    if 'str' in params:
        string = params['str']
        result['lowercase'] = sum(map(str.islower, string))
        result['digits']    = sum(map(str.isdigit, string))
        result['uppercase'] = sum(map(str.isupper, string))
        result['special']   = sum(not char.isalpha() and not char.isdigit() for char in string)
    if 'num1' in params and 'num2' in params:
        a, b = params['num1'], params['num2']
        result['sum'] = a + b
        result['sub'] = a - b
        result['mul'] = a * b
        result['div'] = a // b
        result['mod'] = a % b
    return jsonify(result)