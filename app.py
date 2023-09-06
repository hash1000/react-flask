from markupsafe import escape
from flask import Flask, abort
from flask import Flask, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)



users = {
    1: {'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'},
    2: {'id': 2, 'name': 'Jane Smith', 'email': 'janesmith@example.com'}
}


@app.route('/users', methods=['GET'])
def get_all_users():
    return users




