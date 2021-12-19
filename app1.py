# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 18:40:03 2021

@author: info
"""


from flask import Flask, render_template, request
import jsonify
import requests
import os
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('cgpa_for_stud.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        SEM1 =float(request.form['1_SEM'])
        SEM2=float(request.form['2_SEM'])
        SEM3=float(request.form['3_SEM'])
        SEM4=float(request.form['4_SEM'])
        prediction=model.predict([[SEM1,SEM2,SEM3,SEM4]])
        output=np.round(prediction[0],2)
        if output<0 or output>10:
            return render_template('index.html',prediction_text="PLEASE ENTER  CORRECT DETAILS")
        else:
            return render_template('index.html',prediction_text="Your final CGPA could be  {} ".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)