# app.py - a minimal flask api using flask restful
from flask import flask
from flask restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {'hello': "first pipeline"}

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')        
