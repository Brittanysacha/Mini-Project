from flask import Flask, request, jsonify
import traceback
import pandas as pd
import pickle

# App definition
app = Flask(__name__)

# Importing models
with open('model_columns.pkl', 'rb') as file:
    model_columns = pickle.load(file)

with open('process_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def welcome():
    return "Welcome! Use the below application for loan prediction"

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'GET':
        return "Prediction page. Try inputting your parameters to get specific prediction."

    if request.method == 'POST':
        try:
            json_ = request.json
            query = pd.DataFrame(json_)
            query = query.reindex(columns=model_columns, fill_value=0)
                
            prediction = list(model.predict(query))

            return jsonify({
                "prediction":str(prediction)
            })

        except:
            return jsonify({
                "trace": traceback.format_exc()
            })

if __name__ == "__main__":
    app.run(debug=True)