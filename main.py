from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


class Welcome(Resource):
    def get(self):
        return "Welcome to the Youtube Converter Service"


api.add_resource(Welcome, "/api")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='3001',debug=True)
