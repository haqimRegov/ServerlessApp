from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
import json
from ast import literal_eval
from locmod import update_user_info,getUserDataBmi,calculateBMI,inserBmiData,getDataBmiTable
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app,resources={r"/*": {"origins":"*"}})



@app.route('/hello_vijay',methods=['GET'])
def hello_vijay():

    return "Hello Vijay Welcome to Serverless"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)