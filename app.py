import json
from flask import Flask, request, jsonify

import numpy as np
import os
import pandas as pd

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

waitList_n = 0
@app.route('/join_waitlist', methods=['POST'])
def joinWaitList():
    data = request.get_json()
    email_address = data['email']
    print('email received : ',email_address)
    emails_file_name = 'email_addresses.csv'
    if os.path.isfile(emails_file_name)==False:
        print('File not found! Creating the file...')
        email_df = pd.DataFrame(columns=['Email'])
        email_df.to_csv(emails_file_name,sep=',',index=False)

    email_df = pd.DataFrame([email_address])
    email_df.to_csv(emails_file_name, mode='a', header=False, index=False)
    waitList_n =+ 1
    return jsonify({'status' : 'success'})
    
@app.route('/get_waitlist_count', methods=['GET'])
def getWaitListCount():
    if os.path.isfile('email_addresses.csv')==True:
        email_df = pd.read_csv('email_addresses.csv')
        return jsonify({'waitList_count' : str(len(email_df))})
    return jsonify({'waitList_count' : str(0)})

users = {
    1: {'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'},
    2: {'id': 2, 'name': 'Jane Smith', 'email': 'janesmith@example.com'}
}


@app.route('/users', methods=['GET'])
def get_all_users():
    return users





app.run()