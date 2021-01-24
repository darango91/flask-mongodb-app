"""
Flask App main file

Author: Diego Arango - @darango91
"""

from flask import Flask
from flask_pymongo import PyMongo

from constants import MONGO_DB_CONNECTION
from handlers.routes import configure_routes

app = Flask(__name__)

app.config["MONGO_URI"] = MONGO_DB_CONNECTION
mongo = PyMongo(app)

configure_routes(app, mongo)

if __name__ == "__main__":
    app.run(debug=True)
