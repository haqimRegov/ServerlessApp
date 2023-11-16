from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
import json
import logging
from ast import literal_eval
from locmod import update_user_info,getUserDataBmi,calculateBMI,inserBmiData,getDataBmiTable
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app,resources={r"/*": {"origins":"*"}})



@app.route('/hello_vijay',methods=['GET'])
def hello_vijay():
    print("Endpoint accessible")

    return "Hello Vijay Welcome to Serverless"

@app.route('/')
def index():
    user_ip = request.remote_addr  # Get the user's IP address
    logging.info(f'User with IP address {user_ip} visited the website.')
    
    # Your other web application code here
    return "Hello, World !"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
