## API Documentation

### Loan Prediction API

The Loan Prediction API provides the functionality to predict loan approval based on various input parameters.

### Endpoints

#### GET /predict

This endpoint accepts GET requests and provides loan prediction based on query parameters.

**Request Parameters**

| Parameter             | Type   | Description                                  |
| --------------------- | ------ | -------------------------------------------- |
| `gender`              | string | Gender of the applicant                      |
| `married`             | string | Marital status of the applicant              |
| `dependents`          | string | Number of dependents of the applicant        |
| `education`           | string | Education level of the applicant             |
| `self_employed`       | string | Self-employment status of the applicant      |
| `applicant_income`    | number | Income of the applicant                      |
| `coapplicant_income`  | number | Income of the co-applicant                    |
| `loan_amount`         | number | Loan amount requested                         |
| `loan_amount_term`    | number | Term of the loan in months                    |
| `credit_history`      | number | Credit history of the applicant               |
| `property_area`       | string | Property area of the applicant                |
| `loan_term_category`  | string | Categorical representation of the loan term   |


**Example Request**

GET /predict?gender=Male&married=Yes&dependents=2&education=Graduate&self_employed=No&applicant_income=5000&coapplicant_income=0&loan_amount=128&loan_amount_term=360&credit_history=1&property_area=Urban&loan_term_category=Long-term

**Example Response**

HTTP/1.1 200 OK
Content-Type: application/json

{
"prediction": "['Y']"
}


#### POST /predict

This endpoint accepts POST requests and provides loan prediction based on a JSON payload.

**Request Parameters**

The request body should contain a JSON object with the same parameters as described for the GET endpoint.

**Example Request**


POST /predict
Content-Type: application/json

{
"gender": "Male",
"married": "Yes",
"dependents": "2",
"education": "Graduate",
"self_employed": "No",
"applicant_income": 5000,
"coapplicant_income": 0,
"loan_amount": 128,
"loan_amount_term": 360,
"credit_history": 1,
"property_area": "Urban",
"loan_term_category": "Long-term"
}

**Example Response**

HTTP/1.1 200 OK
Content-Type: application/json

{
"prediction": "['Y']"
}