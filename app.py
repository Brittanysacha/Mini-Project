from flask import Flask, request, jsonify
import traceback
import pandas as pd
from joblib import load
from notebooks.preprocess import PreprocessData, DropAndRenameColumns
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
        try:
            gender = request.args.get('gender')
            married = request.args.get('married')
            dependents = request.args.get('dependents')
            education = request.args.get('education')
            self_employed = request.args.get('self_employed')
            applicant_income = request.args.get('applicant_income')
            coapplicant_income = request.args.get('coapplicant_income')
            loan_amount = request.args.get('loan_amount')
            loan_amount_term = request.args.get('loan_amount_term')
            credit_history = request.args.get('credit_history')
            property_area = request.args.get('property_area')
            loan_term_category = request.args.get('loan_term_category')

            query = pd.DataFrame({
                'Gender': [gender],
                'Married': [married],
                'Dependents': [dependents],
                'Education': [education],
                'Self_Employed': [self_employed],
                'ApplicantIncome': [applicant_income],
                'CoapplicantIncome': [coapplicant_income],
                'LoanAmount': [loan_amount],
                'Loan_Amount_Term': [loan_amount_term],
                'Credit_History': [credit_history],
                'Property_Area': [property_area],
                'Loan_Term_Category': [loan_term_category]
            })

            query = query.reindex(columns=model_columns, fill_value=0)

            # Print the columns in the query DataFrame
            print("Query columns:", query.columns)

            prediction = list(model.predict(query))

            return jsonify({
                "prediction": str(prediction)
            })

        except:
            return jsonify({
                "trace": traceback.format_exc()
            })

    if request.method == 'POST':
        try:
            json_ = request.json
            query = pd.DataFrame(json_, index=[0])
            query = query.reindex(columns=model_columns, fill_value=0)

            # Print the columns in the query DataFrame
            print("Query columns:", query.columns)

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
