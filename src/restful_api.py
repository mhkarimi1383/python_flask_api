from flask import Flask, jsonify, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def Home():
    """Home page to show usage of API"""
    resp = render_template('index.html')
    return resp

class Ping(Resource):
    """Simple ping-pong"""
    def get(self):
        """Get Method for ping-pong"""
        resp = jsonify({"response": 'Pong!'})
        return resp

api.add_resource(Ping, '/ping')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
