
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/api/add', methods=['GET'])

def add():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return jsonify({'result': num1 + num2})

if __name__ == '__main__':
    app.run(debug=True)
