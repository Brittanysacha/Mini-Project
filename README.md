# Mini-project IV

## Project/Goals
The objective of this project was to create a loan prediction algorithm as a crucial component of a pipeline, with the aim of determining an individual's eligibility for loan approval. This predictive algorithm was intended to be deployed onto an AWS instance.

## Hypothesis

Preliminary hypotheses were formulated regarding the factors influencing loan approval for applicants. The following hypotheses were proposed:

### Applicants more likely to be approved for a loan: 
- **Hypothesis 1:** Applicants who possess a credit history are more likely to receive a loan due to a demonstrated track record of financial responsibility and repayment capability.
- **Hypothesis 2:** Applicants with higher applicant and co-applicant incomes are more likely to receive a loan as their higher income levels indicate greater financial stability and ability to meet repayment obligations.
- **Hypothesis 3:** Applicants with a higher level of education are more likely to receive a loan as education level can be associated with higher earning potential and financial stability.
- **Hypothesis 4:** Properties located in urban areas with high growth prospects are more likely to result in loan approval because these areas tend to offer more favorable economic conditions and potential for property value appreciation.
- **Hypothesis 5:** Applicants with longer loan terms are more likely to receive a loan as longer loan durations provide a greater opportunity for the bank to collect interest and reduce the risk of default, thereby increasing the likelihood of loan approval.

### Applicants less likely to be approved for a loan:
- **Hypothesis 6:** Applicants with a higher number of dependents are less likely to receive a loan, as their increased financial obligations may limit their ability to meet loan repayment requirements.
- **Hypothesis 7:** Applicants with a low income-to-loan ratio, even if they have a co-applicant, are less likely to receive a loan as it indicates a potential inability to manage loan payments based on their available income.
- **Hypothesis 8:** Applicants who are self-employed are less likely to receive a loan as their income may be less stable and there is a perceived higher risk associated with self-employment.
- **Hypothesis 9:** Applicants with a shorter loan amount term that results in higher monthly payments are less likely to receive a loan due to the potential strain on their financial resources and their ability to manage higher payment obligations, making it less attractive for banks as the interest received may be lower and may not outweigh the associated risks.
- **Hypothesis 10:** Applicants without a credit history are less likely to receive a loan as there is no prior evidence to assess their creditworthiness and repayment behavior.

To test these hypotheses, exploratory data analysis (EDA) will be conducted on the loan data, examining the relationship between these factors and loan approval. Additionally, machine learning algorithms will be applied to develop a loan prediction model based on the identified factors. The accuracy of the model will be assessed using appropriate evaluation metrics, and cross-validation techniques will be employed to ensure robustness.

## EDA 
The next step of the project involved conducting Exploratory Data Analysis (EDA) to gain deeper insights into individuals' information from loan applications. 

During the analysis, the loan amount distribution was examined and found to exhibit non-normal behavior, with a significant right-skew and presence of extreme values. 

![Applicant distribution (no log)](https://github.com/Brittanysacha/Mini-Project/blob/master/images/Applicant%20distribution%20(no%20log).png)

![Co-applicant distribution (no log)](https://github.com/Brittanysacha/Mini-Project/blob/master/images/Co-applicant%20distribution%20(no%20log).png)

To address this, a log transformation was applied to create a more balanced distribution by smoothing out the extreme values.

![Combined income distribution (with log transformation)](https://github.com/Brittanysacha/Mini-Project/blob/master/images/Combined%20income%20distribution%20(with%20log%20transformation).png)

In addition, a pivot chart analysis was performed to explore factors influencing loan approval. 

![Pivot Chart Loan Factors](https://github.com/Brittanysacha/Mini-Project/blob/master/images/Pivot%20Chart%20EDA.png)

The results indicated that gender, marital status, dependents, education level, and credit history had a substantial impact on the likelihood of loan approval. Specifically, being male, married, having no dependents, holding a graduate degree, and having a credit history were associated with higher approval rates. Surprisingly, the type of property and the number of children showed minimal influence on loan approval.

Despite potential arguments for bias, all columns, including gender and marital status, were retained in the analysis. This decision was made to ensure transparency, maintain the dataset's integrity, and enable a comprehensive examination of the data.

These findings from the EDA, log transformation, pivot chart analysis, and decision to retain all columns contribute to a thorough understanding of the dataset and provide valuable insights for loan approval processes.

## Process

### Data Cleaning
The next step in the data analysis process involved data cleaning to address missing values in the dataset. Rather than discarding rows with missing values or imputing them with simple measures like mean or mode, a combination of techniques such as K-nearest neighbors (KNN) and logistic regression was used to impute the missing values. This approach was chosen to maintain the integrity of the data and prevent potential bias.

### Data Wrangling
Following data cleaning, the focus shifted to data wrangling. Categorical variables were transformed into binary representations, where applicable, by assigning values of 0 or 1. For variables with more than two options, label encoding was employed to encode them into numerical values.

### Feature Engineering
In the feature engineering phase, several transformations were applied. Log transformations were performed on certain variables to normalize their distributions and handle skewness. Additionally, income variables were combined to create a comprehensive measure of total income. The loan term was transformed into three categories: short-term (less than 5 years), medium-term (5-10 years), and long-term (10 years or more).

### Model Building
Moving on to model building, a random forest classifier was selected as the predictive model. This ensemble learning method utilizes multiple decision trees to make accurate predictions.

### Model Testing
Finally, in the model testing stage, a pipeline was constructed to streamline the data preprocessing and modeling steps. The pipeline was evaluated to assess its performance in accurately predicting the probability of a loan being approved or not approved.

### Building the Flask Application

The Flask application was developed to provide an interface for loan prediction based on user input. The application utilizes the Flask framework and includes routes to handle different endpoints. The necessary models and preprocessing steps are loaded into the application using the `joblib` library. The `model_columns` file ensures that the input data aligns correctly with the model's feature columns.

The `/predict.html` route renders an HTML form that allows users to input loan prediction parameters. When the form is submitted, it makes a GET request to the `/predict` endpoint.

The `/predict` endpoint handles both GET and POST requests. It retrieves the loan prediction parameters from the request and creates a query DataFrame. The query DataFrame is then transformed to match the model's feature columns. The loan prediction is generated using the loaded model, and the result is returned as a JSON response.

### Building the HTML Portal

The HTML portal, named `predict.html`, provides a user-friendly form for inputting loan prediction parameters. It uses HTML and JavaScript to collect user input and send AJAX requests to the Flask API endpoint.

The form allows users to input various loan prediction parameters such as gender, marital status, education, income, loan amount, and credit history. When the form is submitted, an AJAX request is sent to the `/predict` endpoint, passing the input data as query parameters.

The response from the API is displayed on the web page, showing the predicted loan approval status. The portal also includes a footer section that provides a list of accepted inputs for each parameter.

### API Documentation

The Loan Prediction API provides functionality for predicting loan approval based on user input. It includes two endpoints: `/predict` for handling loan prediction requests and `/predict.html` for rendering the loan prediction form.

The `/predict` endpoint accepts GET and POST requests. For GET requests, the loan prediction parameters are passed as query parameters. For POST requests, the parameters are included in the JSON payload.

To make a loan prediction, the API requires input parameters such as gender, marital status, dependents, education, income, loan amount, loan term, credit history, property area, and loan term category.

Detailed documentation for the Loan Prediction API can be found in the `AWS_API_Loan.md` file in the project repository.

## Results/Demo

### Important Features

To test the API, various loan prediction scenarios were executed using curl commands. The results showed the predicted loan approval status for different input combinations.

For example, a loan request with a male applicant who is married, has 2 dependents, a graduate education, no self-employment, an applicant income of 5000, no coapplicant income, a loan amount of 128, a loan amount term of 360, a credit history of 1, an urban property area, and a long-term loan term category resulted in a prediction of loan approval (`['Y']`). This was tested in both as a local instance and an AWS instance.

![AWS Instance]()


These test results demonstrate the functionality and accuracy of the Loan Prediction API in predicting loan approval based on the provided input parameters.

From the predictive model, several important features were identified for determining loan approval. These were determine from the output of the model decision tree:

![Decision Tree]()

- Credit History: Having or not having a credit history was found to be the most significant factor, accounting for 42% of the variance in loan approval decisions.
- Property Area: The property area, including urban, semiurban, and rural locations, also played a significant role in loan approval.
- Marital Status, Dependents, Education: These demographic factors were found to be influential in the loan approval process.
- Loan Term: The duration of the loan term, categorized into short-term, medium-term, and long-term, was identified as another important feature.

The decision tree algorithm learned different combinations of these features to classify loan applicants as eligible (class Y) or not eligible (class N) based on the available data.

### Performance Metrics
The model's performance was evaluated using the following metrics:

- Accuracy: The model achieved an accuracy of 70.73%, indicating that it correctly predicted the loan approval status for approximately 70.73% of the cases.
- Precision: With a precision of 74.44%, the model demonstrated a relatively good ability to accurately identify loan approvals among all cases predicted as positive.
- Recall: The recall value, also known as sensitivity, was 83.75%, indicating a high ability of the model to correctly detect loan approvals among all actual positive cases.
- F1-Score: The F1-score, which is the harmonic mean of precision and recall, was 78.82%. This balanced measure highlights the model's overall performance in capturing both precision and recall.

![Metrics)](https://github.com/Brittanysacha/Mini-Project/blob/master/images/Metric%20Success.png)

These performance metrics provide insights into the model's ability to predict loan approval outcomes accurately and effectively.

## Challanges 
(discuss challenges you faced in the project)

## Future Goals
(what would you do if you had more time? are there any potential issues/biases with your model/use case?)