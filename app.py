from flask import Flask, request, jsonify
import traceback
import pandas as pd
from joblib import load
from preprocess import PreprocessData
from sklearn.base import BaseEstimator, TransformerMixin

# App definition
app = Flask(__name__)

# Importing models
model_columns = load('notebooks/model_columns.joblib')
model = load('notebooks/process_model.joblib')

@app.route('/')
def welcome():
    return "Welcome! Use the below application for loan prediction"

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return "Prediction page. Try inputting your parameters to get a specific prediction."

    if request.method == 'POST':
        try:
            json_ = request.json
            query = pd.DataFrame(json_)
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(model.predict(query))

            return jsonify({
                "prediction": str(prediction)
            })

        except:
            return jsonify({
                "trace": traceback.format_exc()
            })

if __name__ == "__main__":
    app.run(debug=True)


# push this app to git repo and then clone the whole repository on the AWS terminal
# make new AWS2 instance - install python (sudo app python) - clone repo apt-get
# On AWS instancw run app.py (then get that instances IP address) send a request http:get request