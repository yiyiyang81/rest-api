from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app) #wrap app in the api(restful)

class Grape(Resource):
    def get(self):
        return {"data":"Gilbert Grape"}

api.add_resource(Grape, "/hellowworld")

if __name__ == "__main__":
    app.run(debug=True) #debug mode