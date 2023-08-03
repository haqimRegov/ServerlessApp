from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
import json
from ast import literal_eval
from src.app import update_user_info,getUserDataBmi,calculateBMI,inserBmiData,getDataBmiTable
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/add_user',methods=['GET','POST'])
def addUser():
    data=request.json
    print(data)
    update_user_info(data)
    userdict=getUserDataBmi(data)
    bmi=calculateBMI(userdict)
    updatedb=inserBmiData(bmi)
    return (bmi,updatedb)

@app.route('/getBmi',methods=['GET','POST'])
def getbmi():
    data=request.json
    print(data)
    print(type(data))
    queryBmiTable=getDataBmiTable(data)
    print(queryBmiTable)
    
    return queryBmiTable

if __name__ == '__main__':
    app.run(debug=True)