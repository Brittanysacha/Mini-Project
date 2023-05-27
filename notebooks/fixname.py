def drop_and_rename_columns(df):
    # Drop the specified columns
    columns_to_drop = ['Loan_ID', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']
    df = df.drop(columns_to_drop, axis=1)
    
    # Define the mapping dictionary for column name conversions
    column_mapping = {
        'Gender': 'gender',
        'Married': 'married',
        'Dependents': 'dependents',
        'Education': 'education',
        'Self_Employed': 'self_employed',
        'LoanAmount': 'loan_amount',
        'Loan_Amount_Term': 'loan_amount_term',
        'Credit_History': 'credit_history',
        'Loan_Status': 'loan_status',
        'property_area_Rural': 'property_area_rural',
        'property_area_Semiurban': 'property_area_semiurban',
        'property_area_Urban': 'property_area_urban',
        'Loan_Term_Category_Short-term': 'loan_term_short',
        'Loan_Term_Category_Medium-term': 'loan_term_medium',
        'Loan_Term_Category_Long-term': 'loan_term_long',
        'Loan_Status ': 'loan_status'
    }

    # Rename the columns using the mapping dictionary
    df.rename(columns=column_mapping, inplace=True)
    
    return df
