from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app) #wrap app in the api(restful)


name_args = reqparse.RequestParser()
name_args.add_argument("ID", type=str, help="ID of the employee", required = True)
name_args.add_argument("name", type=str, help="Name of the employee", required=True)
name_args.add_argument("position", type=str, help="Position of the employee")

names = {}

# "Leslie":{"name":"Leslie", "ID": "001", "position":"Co-Founder"}, 
#         "Sarah":{"name":"Sarah", "ID": "002", "position": "CEO"}

def error_invalid_employee(name):
    if name not in names:
        abort(404, message ="Employee not found")


class HelloWorld(Resource):
    def get(self, name):
        error_invalid_employee(name)
        return names[name]

    def register(self, name):
        args = name_args.parse_args()   #gets input elements from names
        names[name] = args
        return names[name], 201     #201 for succesful creation

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True) #debug mode
