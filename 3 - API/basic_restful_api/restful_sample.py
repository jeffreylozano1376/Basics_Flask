from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"jeffrey": {"age": 29, "gender": "male"},
        "ken": {"age": 27, "gender": "female"}}

# Create Resource
class HelloWorld(Resource):
    def get(self, name):
        return names[name]

# Register Resource (Class, "API Endpoint/<parameter>")
api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__=="__main__":
    app.run(debug=True)