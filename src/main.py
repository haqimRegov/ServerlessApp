from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
import json
from ast import literal_eval
from src.app import update_user_info,getUserDataBmi,calculateBMI,inserBmiData,getDataBmiTable
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app,resources={r"/*": {"origins":"*"}})

@app.route('/add_user',methods=['GET','POST'])
def addUser():
    data=request.json
    print(data)
    update_user_info(data)
    userdict=getUserDataBmi(data)
    bmi=calculateBMI(userdict)
    updatedb=inserBmiData(bmi)
    return (bmi,updatedb)

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

@app.route('/hello_vijay',methods=['GET'])
def hello_vijay():

    return "Hello Vijay Welcome to Serverless"

@app.route('/ainnurtest',methods=['GET'])
def ainnurtest():
    data={
        "name":"Ainnur",
        "age":"20",
        "height":"167",
        "adress":"pokemon",
    }

    return data

if __name__ == '__main__':
    app.run(debug=True)