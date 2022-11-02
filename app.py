from flask import Flask, render_template, request
import pickle
import numpy as np
import joblib

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'model/modelFDM.pickle'
    print(filename)
    print("Aroooooooooooooooooooooooooooooooooo")

    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])

    print(pred_value)
    return pred_value


@app.route('/', methods=['POST', 'GET'])
def index():

    pred_value = 0
    if request.method == 'POST':
     
        Date = request.form['Date']
        OPUNIQUECARRIER = request.form['OPUNIQUECARRIER']
        ORIGIN = request.form['ORIGIN']
        DEST = request.form['DEST']
        DEPTIME = request.form['DEPTIME']
        ARRTIME = request.form['ARRTIME']
        DISTANCE = request.form['DISTANCE']

        feature_list = []

        feature_list.append(int(Date))
        feature_list.append(int(OPUNIQUECARRIER))
        feature_list.append(int(ORIGIN))
        feature_list.append(int(DEST))
        feature_list.append(float(DEPTIME))
        feature_list.append(float(ARRTIME))
        feature_list.append(float(DISTANCE))

        pred_value = prediction(feature_list)




        if pred_value == 1:
            pred_value = 'Flight Will Delay'
        else :
            pred_value = 'Flight Will Not Delay'

    return render_template('index.html',pred_value=pred_value,Date=Date,OPUNIQUECARRIER = OPUNIQUECARRIER, ORIGIN =ORIGIN, DEST=DEST ,DEPTIME=DEPTIME ,ARRTIME= ARRTIME ,DISTANCE =DISTANCE)

    
if __name__ == '__main__':
    app.run(debug=True)