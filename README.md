# Mini-project IV

### [Assignment](assignment.md)

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

![Applicant distribution (no log)](image_path)

![Co-applicant distribution (no log)](image_path)

To address this, a log transformation was applied to create a more balanced distribution by smoothing out the extreme values.

![Combined income distribution (with log transformation)](image_path)

In addition, a pivot chart analysis was performed to explore factors influencing loan approval. 

![Pivot Chart Loan Factors](image_path)

The results indicated that gender, marital status, dependents, education level, and credit history had a substantial impact on the likelihood of loan approval. Specifically, being male, married, having no dependents, holding a graduate degree, and having a credit history were associated with higher approval rates. Surprisingly, the type of property and the number of children showed minimal influence on loan approval.

Despite potential arguments for bias, all columns, including gender and marital status, were retained in the analysis. This decision was made to ensure transparency, maintain the dataset's integrity, and enable a comprehensive examination of the data.

These findings from the EDA, log transformation, pivot chart analysis, and decision to retain all columns contribute to a thorough understanding of the dataset and provide valuable insights for loan approval processes.

## Process
(fill in what you did during EDA, cleaning, feature engineering, modeling, deployment, testing)
### (your step 1)
### (your step 2)

## Results/Demo
(fill in your model's performance, details about the API you created, and (optional) a link to an live demo)

## Challanges 
(discuss challenges you faced in the project)

## Future Goals
(what would you do if you had more time? are there any potential issues/biases with your model/use case?)