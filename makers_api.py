from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Create class -> Create endpoint
class Users(Resource):
    pass

api.add_resource(Users, '/users') # 