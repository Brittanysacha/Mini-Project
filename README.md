# Mini-project II

## Project Goals
The objective of this project was to create a loan prediction algorithm as a crucial component of a pipeline, with the aim of determining an individual's eligibility for loan approval. This predictive algorithm was intended to be deployed locally and as a AWS instance.

## Table of Contents
1. [Hypothesis](#hypothesis)
   - [Applicants more likely to be approved for a loan](#applicants-more-likely-to-be-approved-for-a-loan)
   - [Applicants less likely to be approved for a loan](#applicants-less-likely-to-be-approved-for-a-loan)
2. [EDA](#eda)
3. [Process](#process)
   - [Data Cleaning](#data-cleaning)
   - [Data Wrangling](#data-wrangling)
   - [Feature Engineering](#feature-engineering)
   - [Model Building](#model-building)
   - [Model Testing](#model-testing)
   - [Building the Flask Application](#building-the-flask-application)
   - [Building the HTML Portal](#building-the-html-portal)
   - [API Documentation](#api-documentation)
4. [Results](#results)
   - [Local and AWS Deployment](#local-and-aws-deployment)
   - [Important Features](#important-features)
   - [Performance Metrics](#performance-metrics)
5. [Challenges](#challenges)
6. [Future Goals](#future-goals)


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

To test these hypotheses, exploratory data analysis (EDA) was conducted on the loan data, examining the relationship between different demographic and personal factors and loan approval. This analysis will guide further machine learning algorithm development in an attept to create an accurate loan prediction model. The accuracy of the model will be assessed using appropriate evaluation metrics, and cross-validation techniques will be employed to ensure robustness.

## EDA 
This stage of the project entailed conducting Exploratory Data Analysis (EDA) to gain deeper insights into individuals' information from loan applications. Some key insights from this process, are displayed below.

**1.)**  During the analysis, the loan amount distribution was examined and found to exhibit non-normal behavior, with a significant right-skew and presence of extreme values. 

![Applicant distribution (no log)](https://github.com/Brittanysacha/Mini-Project/blob/master/images/Applicant%20distribution%20(no%20log).png)

![Co-applicant distribution (no log)](https://github.com/Brittanysacha/Mini-Project/blob/master/images/Co-applicant%20distribution%20(no%20log).png)

**2.)** To address non-normal distribution, a log transformation was applied to create a more balanced distribution by smoothing out the extreme values.

![Combined income distribution (with log transformation)](https://github.com/Brittanysacha/Mini-Project/blob/master/images/Combined%20income%20distribution%20(with%20log%20transformation).png)

**3.)** A pivot chart analysis was performed to explore factors influencing loan approval. 

![Pivot Chart Loan Factors](https://github.com/Brittanysacha/Mini-Project/blob/master/images/Pivot%20Chart%20EDA.png)

The results indicated that gender, marital status, dependents, education level, and credit history had a substantial impact on the likelihood of loan approval. Specifically, being male, married, having no dependents, holding a graduate degree, and having a credit history were associated with higher approval rates. Surprisingly, the type of property and the number of children showed minimal influence on loan approval.

**In sum:**
Despite potential arguments for bias, all columns, including gender and marital status, were retained in the analysis. This decision was made to ensure transparency, maintain the dataset's integrity, and enable a comprehensive examination of the data. The findings from the EDA, log transformation, pivot chart analysis, and decision to retain all columns contribute to a thorough understanding of the dataset and provide valuable insights for loan approval processes.

## Process

### Data Cleaning
The next step in the data analysis process involved data cleaning to address missing values in the dataset. Rather than discarding rows with missing values or imputing them with simple measures like mean or mode, a combination of techniques such as K-nearest neighbors (KNN) and logistic regression was used to impute the missing values. This approach was chosen to maintain the integrity of the data and prevent potential bias.

### Data Wrangling
Following data cleaning, the focus shifted to data wrangling. Categorical variables were transformed into binary representations, where applicable, by assigning values of 0 or 1. For variables with more than two options, label encoding was employed to encode them into numerical values.

### Feature Engineering
In the feature engineering phase, several transformations were applied. Log transformations were performed on certain variables to normalize their distributions and handle skewness. Additionally, income variables were combined to create a comprehensive measure of total income. The loan term was transformed into three categories: short-term (less than 5 years), medium-term (5-10 years), and long-term (10 years or more).

### Model Building
For model building, a random forest classifier was selected as the predictive model. This ensemble learning method utilised multiple decision trees to make accurate predictions.

### Model Testing
In the model testing stage, a pipeline was constructed to streamline the data preprocessing and modeling steps. The pipeline was evaluated to assess its performance in accurately predicting the probability of a loan being approved or not approved.

### Building the Flask Application

The Flask application was developed to provide an interface for loan prediction based on user input. The application utilised the Flask framework and included routes to handle different endpoints. The necessary models and preprocessing steps were loaded into the application using the `joblib` library. The `model_columns` file ensures that the input data aligns correctly with the model's feature columns.

The `/predict.html` route rendered an HTML form that allows users to input loan prediction parameters. When the form is submitted, it makes a GET request to the `/predict` endpoint.

The `/predict` endpoint handles both GET and POST requests. It retrieves the loan prediction parameters from the request and creates a query DataFrame. The query DataFrame is then transformed to match the model's feature columns. The loan prediction is generated using the loaded model, and the result is returned as a JSON response.

### Building the HTML Portal

To try and provide a means to allow access to the form entry more directly, I attempted to build a HTML portal, named `predict.html`. This portal provides a user-friendly form for inputting loan prediction parameters. It uses HTML and JavaScript to collect user input and send AJAX requests to the Flask API endpoint.

The form allows users to input various loan prediction parameters such as gender, marital status, education, income, loan amount, and credit history. When the form is submitted, an AJAX request is sent to the `/predict` endpoint, passing the input data as query parameters.

The intention behind this portal was to make sure a response from the API was displayed on the web page when hitting submit, showing the predicted loan approval status. The portal also included a footer section that provides a list of accepted inputs for each parameter. Further steps would need to be taken to connect the AWS instance to the HTML portal.

![HTML](https://github.com/Brittanysacha/Mini-Project/blob/master/images/HTML%20Preview.png)

### API Documentation

I further created an API documentation [markdown](https://github.com/Brittanysacha/Mini-Project/blob/master/templates/AWS_API_Loan.md). The Loan Prediction API provides functionality for predicting loan approval based on user input. It includes two endpoints: `/predict` for handling loan prediction requests and `/predict.html` for rendering the loan prediction form.

To make a loan prediction, the API requires input parameters such as gender, marital status, dependents, education, income, loan amount, loan term, credit history, property area, and loan term category.

## Results

### Local and AWS Deployment

To test the API, various loan prediction scenarios were executed using curl commands. The results showed the predicted loan approval status for different input combinations.

For example, a loan request with a male applicant who is married, has 2 dependents, a graduate education, no self-employment, an applicant income of 5000, no coapplicant income, a loan amount of 128, a loan amount term of 360, a credit history of 1, an urban property area, and a long-term loan term category resulted in a prediction of loan approval (`['Y']`). This was tested in both as a local instance and an AWS instance.

![AWS Instance](https://github.com/Brittanysacha/Mini-Project/blob/master/images/ECS%20Instance%20.png)

These test results demonstrate the functionality and accuracy of the Loan Prediction API in predicting loan approval based on the provided input parameters.

### Important Features
From the predictive model, several important features were identified for determining loan approval. These were determine from the output of the model decision tree:

![Decision Tree](https://github.com/Brittanysacha/Mini-Project/blob/master/images/Decision%20Tree.png)

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
In this project, there were certain limitations that should be taken into consideration. Firstly, the combination of complex cleaning and feature engineering functions within a pipeline posed a significant challenge. It required careful handling to ensure the smooth integration of these processes, as well as a lot of debugging to make sure the different elements occered in the right order and fit together.

Additionally, the availability of limited data restricted the use of more sophisticated models. With a smaller dataset, there was a need to exercise caution to avoid overfitting and ensure the model's generalizability. Finally, despite implementing imputation techniques to address missing data, the overall accuracy of the results may have been affected by the incompleteness of the available data. This limitation highlights the importance of having comprehensive and reliable data to achieve more accurate predictions.

## Future Goals
In the future, there are several goals that can be pursued to enhance the model and its capabilities. Firstly, running the model on a larger dataset can provide more data points and improve the prediction accuracy. This can be achieved by gathering additional loan application data or expanding the existing dataset.

Another important goal is conducting further hyperparameter tuning. Fine-tuning the model's parameters can optimise its performance and potentially increase the prediction level. This process involves systematically exploring different parameter combinations to identify the optimal settings for the model.

Additionally, exploring advanced techniques such as training models on specific data clusters or leveraging other models can be considered. This approach can potentially capture more nuanced patterns and improve the model's predictive capabilities.

Furthermore, connecting the HTML browser with the AWS instance can enhance the accessibility and usability of the application. This would enable users to access and utilise the loan prediction system remotely, increasing its practicality and reach.


For a high-level overview, please refer to this [short presentation](https://www.canva.com/design/DAFkClSAw-s/h6af3XX8ehkz54VzbrbA_Q/edit?utm_content=DAFkClSAw-s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

