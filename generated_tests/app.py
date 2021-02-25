from flask import Flask, jsonify
from flasgger import Swagger
from flasgger import SwaggerView
from flasgger import Schema
from flasgger import fields


app = Flask(__name__)
swagger = Swagger(app)


class ImagesView(SwaggerView):
    parameters = []
    responses = {
        200: {
            "description": "A list of colors (may be filtered by palette)",
            "schema": Palette
        }
    }