# app.py
from flask import Flask, request, jsonify
import os
from scripts.entry import init

init()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'test': true})

if __name__ == '__main__':
    app.run(debug=True)
