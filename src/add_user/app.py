from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
import json
from ast import literal_eval
from functions import update_user_info,getUserDataBmi,calculateBMI,inserBmiData,getDataBmiTable
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)