# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank = pd.read_csv(path)
bank.head()
categorical_var = bank.select_dtypes(include = 'object')
categorical_var
numerical_var = bank.select_dtypes(include = 'number')
numerical_var
# code starts here






# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],axis = 1)
print(banks.isnull().sum())
bank_mode = banks.mode()
banks = banks.fillna(bank_mode.iloc[0])
print(banks.isnull().sum())
#code ends here



# --------------




# Code starts here
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')



# code ends here



# --------------
# code starts here




loan_approved_se =len(banks[(banks['Self_Employed']== 'Yes') & (banks['Loan_Status'] == 'Y')])
loan_approved_nse = len(banks[(banks['Self_Employed']== 'No') & (banks['Loan_Status'] == 'Y')])
Loan_Status = 614
percentage_se = (loan_approved_se/Loan_Status)*100
percentage_nse = (loan_approved_nse/Loan_Status)*100
# code ends here


# --------------
# code starts here



loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
big_loan_term = loan_term.apply(lambda x : x >= 25).value_counts()
big_loan_term = big_loan_term[1]
big_loan_term


# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()


# code ends here


