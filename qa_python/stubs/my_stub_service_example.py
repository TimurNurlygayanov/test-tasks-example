#!/usr/bin/python3
# -*- encoding=utf8 -*-

# How to run:
#  pip install -U flask
#  python my_stub_service_example.py
#

import flask
from flask import Flask
from flask import request


app = Flask(__name__)

PRODUCTS = [{"id": 76699046,"name": "apple","price": 12.10}]


@app.route('/get_product', methods=['POST'])
def get_product():
    """ This is very simple stub for 'get product' REST API function. """

    # Default response in case
    product = {"code": 404, "description": "Not Found"}

    # Get product ID from request:
    product_id = request.args.get('id', 0)

    # Check parameters:
    if product_id == 0:
        product = {"code": 400,"description": "Bad Request"}

    # Find the product:
    for p in PRODUCTS:
        if p["id"] == product_id:
            product = p

    # Return result:
    return flask.jsonify(product)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
