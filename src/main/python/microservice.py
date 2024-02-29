"""
Microservice Module for DevOps Assignment
This module defines a simple microservice using Flask, a lightweight web framework for Python.
It provides two endpoints:
- /api/hello: Returns a JSON response with a greeting message.
- /api/add: Accepts two numbers as query parameters and returns their sum.

"""
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/api/add', methods=['GET'])

def add():
    """
    Handle GET request for /api/add endpoint.
    Accepts two numbers as query parameters and returns their sum.
    Returns:
        JSON response with the sum of two numbers.
    """
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return jsonify({'result': num1 + num2})

if __name__ == '__main__':
    app.run(debug=True)
