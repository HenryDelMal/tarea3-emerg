from flask import Flask, jsonify, request
import iot_controller
from db import create_tables

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=3000)