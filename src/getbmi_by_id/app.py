from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
import json
from ast import literal_eval
from functions import update_user_info,getUserDataBmi,calculateBMI,inserBmiData,getDataBmiTable
from flask_cors import CORS, cross_origin
app = Flask(__name__)



CORS(app,resources={r"/*": {"origins":"*"}})

@app.route('/getBmi/<nric>',methods=['GET'])
def getbmi_by_id(nric):
    data={
        "nric":nric
    }
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(f'This is the response: {response}')
    user_ic=data["nric"]
    print(user_ic)
    print(type(user_ic))
    queryBmiTable=getDataBmiTable(data)
    print(queryBmiTable)
    
    return queryBmiTable

@app.route('/getBmi',methods=['GET'])
def getbmi():

    return "Kindly Provide your nric"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)