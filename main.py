from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATA_BASE_URI"] = "sqlite:///data/database.db"


if __name__ == "__main__":
    app.run()  # omit debug=True later
    
