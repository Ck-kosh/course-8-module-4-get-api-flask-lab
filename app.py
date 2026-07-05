from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


# Mock data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]


if __name__ == "__main__":
    app.run(debug=True)

