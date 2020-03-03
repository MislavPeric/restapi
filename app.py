from flask import Flask, request
from  flask_restful import Resource, Api
from flask import jsonify

app = Flask(__name__)
api = Api(app)

@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    email = data['email']
    return jsonify({
        email: email
    })