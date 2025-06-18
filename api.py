# quote_api.py
from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    {"author": "Steve Jobs", "quote": "Stay hungry, stay foolish."},
    {"author": "Nelson Mandela", "quote": "It always seems impossible until it’s done."},
    {"author": "Maya Angelou", "quote": "Try to be a rainbow in someone's cloud."}
]

@app.route('/quote', methods=['GET'])
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

