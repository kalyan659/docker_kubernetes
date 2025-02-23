# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:55:12 2025

@author: kalya
"""

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/hello_world')
def hello_world():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000)