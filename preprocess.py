from sklearn.base import BaseEstimator, TransformerMixin

class PreprocessData(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        # Copy the input DataFrame to avoid modifying the original data
        X_transformed = X.copy()
        
        # Impute missing values
        X_transformed['Gender'].fillna('Unknown', inplace=True)
        X_transformed['Married'].fillna('No', inplace=True)
        X_transformed['Dependents'].fillna(0, inplace=True)
        X_transformed['Self_Employed'].fillna('No', inplace=True)
        X_transformed['Dependents'] = X_transformed['Dependents'].replace({'3+': 3})

        # Convert various columns to numeric values
        X_transformed['Gender'] = X_transformed['Gender'].replace({'Male': 0, 'Female': 1, 'Unknown': 2})
        X_transformed['Married'] = X_transformed['Married'].replace({'No': 0, 'Yes': 1})
        X_transformed['Education'] = X_transformed['Education'].replace({'Not Graduate': 0, 'Graduate': 1})
        X_transformed['Self_Employed'] = X_transformed['Self_Employed'].replace({'No': 0, 'Yes': 1})
        X_transformed['Dependents'] = X_transformed['Dependents'].astype(int)

        # Perform ordinal encoding for 'property_area'
        encoder = OrdinalEncoder()
        X_transformed['property_area'] = encoder.fit_transform(X_transformed[['Property_Area']])

        # Drop the original 'Property_Area' column
        X_transformed = X_transformed.drop('Property_Area', axis=1)

        columns_to_impute = ['LoanAmount', 'Loan_Amount_Term', 'Credit_History']
        imputer = KNNImputer(n_neighbors=5)
        
        if X_transformed.shape[0] == 1:
            # Reshape the data to be 2D
            imputed_data = imputer.fit_transform(X_transformed[columns_to_impute].values.reshape(1, -1))
        else:
            imputed_data = imputer.fit_transform(X_transformed[columns_to_impute])
        
        X_transformed[columns_to_impute] = imputed_data

        # Convert the imputed values to a DataFrame
        imputed_df = pd.DataFrame(imputed_data, columns=columns_to_impute, index=X_transformed.index)

        # Merge the imputed values back into the original DataFrame
        X_transformed.drop(columns=columns_to_impute, inplace=True)
        X_transformed = pd.concat([X_transformed, imputed_df], axis=1)

        # Round 'LoanAmount' and 'Loan_Amount_Term' to the nearest whole number
        X_transformed['LoanAmount'] = X_transformed['LoanAmount'].round().astype(int)
        X_transformed['Loan_Amount_Term'] = X_transformed['Loan_Amount_Term'].round().astype(int)

        # Multiply values by 1000 for ApplicantIncome, CoapplicantIncome, and LoanAmount
        X_transformed['ApplicantIncome'] *= 12
        X_transformed['CoapplicantIncome'] *= 12
        X_transformed['LoanAmount'] *= 1000

        # Create categorical variable for Loan_Amount_Term
        X_transformed['Loan_Term_Category'] = pd.cut(X_transformed['Loan_Amount_Term'], bins=[0, 180, 360, np.inf], labels=['Short-term', 'Medium-term', 'Long-term'])

        # Perform ordinal encoding for 'Loan_Term_Category'
        encoder = OrdinalEncoder()
        X_transformed['loan_term_category'] = encoder.fit_transform(X_transformed[['Loan_Term_Category']])

        # Drop the original 'Loan_Term_Category' column
        X_transformed = X_transformed.drop('Loan_Term_Category', axis=1)

        return X_transformed
