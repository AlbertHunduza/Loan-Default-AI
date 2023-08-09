# importing the required libraries
import pandas as pd

# reading the data
loan_data = pd.read_csv('loans50k.csv', encoding='latin1')

# function to preprocess the loan data
def preprocess_loan_data(loan_data):
    # Drop the rows where revolRatio or bcOpen or bcRatio or employment or length or amount column is null
    loan_data.drop(loan_data[loan_data['revolRatio'].isnull() | loan_data['bcOpen'].isnull()
                            | loan_data['bcRatio'].isnull() | loan_data['employment'].isnull()
                            | loan_data['length'].isnull() | loan_data['amount'].isnull()].index, inplace=True)
    
    # edit the verified column to have only two values: 'Verified' and 'Not Verified'
    loan_data['verified'].replace('Source Verified', 'Verified', inplace=True)

    # Drop the 'loanID' column since it doesn't add any value to the model
    loan_data.drop('loanID', axis=1, inplace=True)
    # drop the employment column
    loan_data.drop('employment', axis=1, inplace=True)
    # drop the totalPaid column
    loan_data.drop('totalPaid', axis=1, inplace=True)

    # one-hot encode the 'verified' and home columns
    loan_data = pd.get_dummies(loan_data, columns=['verified'], prefix='verified', drop_first=True)
    loan_data = pd.get_dummies(loan_data, columns=['home'], prefix='home', drop_first=True)
    loan_data = pd.get_dummies(loan_data, columns=['grade'], prefix='grade', drop_first=True)

    # Convert 'term' column to numerical (1 for ' 36 months' and 2 for ' 60 months') and rename it for clarity
    loan_data['term_months'] = loan_data['term'].apply(lambda x: 1 if x == ' 36 months' else 2)
    loan_data.drop('term', axis=1, inplace=True)

    # Define a custom function to extract employment length in years
    def extract_employment_length(length_str):
        if length_str == '< 1 year':
            return 0
        elif length_str == '10+ years':
            return 15  # Or any other suitable value you choose
        else:
            return int(length_str.split()[0])

    # Apply the custom function to the 'length' column and drop the original 'length' column
    loan_data['employment_length_years'] = loan_data['length'].apply(extract_employment_length)
    loan_data.drop(columns=['length'], inplace=True)
    
    # Apply feature hashing to the 'reason' column with 10 bins and drop the original column
    reason_hash_bins = 10
    loan_data['reason_hashed'] = loan_data['reason'].apply(lambda x: hash(x) % reason_hash_bins)
    loan_data.drop(columns=['reason'], inplace=True)

    # Apply feature hashing to the 'state' column with 30 bins and drop the original column
    state_hash_bins = 30
    loan_data['state_hashed'] = loan_data['state'].apply(lambda x: hash(x) % state_hash_bins)
    loan_data.drop(columns=['state'], inplace=True)

    # Convert boolean columns to integers (0 or 1)
    boolean_columns = ['verified_Verified', 'home_OWN', 'home_RENT', 'grade_B', 'grade_C', 'grade_D',
                       'grade_E', 'grade_F', 'grade_G']
    loan_data[boolean_columns] = loan_data[boolean_columns].astype(int)

    # Convert 'status' to binary class labels: 'Safe' and 'Risky'
    status_mapping = {
        'Fully Paid': 'Safe',
        'Current': 'Safe',
        'In Grace Period': 'Risky',
        'Late (16-30 days)': 'Risky',
        'Late (31-120 days)': 'Risky',
        'Charged Off': 'Risky',
        'Default': 'Risky'
    }

    loan_data['status'] = loan_data['status'].map(status_mapping)

    return loan_data

# preprocess the loan data
preprocessed_loan_data = preprocess_loan_data(loan_data)

# save the preprocessed data to a csv file
preprocessed_loan_data.to_csv('preprocessed_loans50k.csv', index=False)
