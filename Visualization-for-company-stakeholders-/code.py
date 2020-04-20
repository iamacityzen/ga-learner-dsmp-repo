# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind = 'bar')

#Code starts here


# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Property Area', fontsize=5)
plt.ylabel('Loan Status', fontsize=5)
#plt.xticks(index = None, label, fontsize=5, rotation=45)
plt.show()


# --------------
#Code starts here
#Plotting an unstacked bar plot
education_and_loan=data.groupby(['Education', 'Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
education_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

#Changing the x-axis label
plt.xlabel('education_and_loan')

#Changing the y-axis label
plt.ylabel('Loan_Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

#Code ends here


# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
graduate.plot(kind = 'density', label = 'Graduate')
not_graduate.plot(kind = 'density', label = 'Not Graduate')






#Code ends here

#For automatic legend display
plt.legend()


# --------------


#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(20,10))

data.plot.scatter(x ='ApplicantIncome', y ='LoanAmount', ax = ax_1)
ax_1.set_title('ApplicantIncome')
data.plot.scatter(x = 'CoapplicantIncome', y = 'LoanAmount',ax = ax_2)
ax_1.set_title('CoapplicantIncome')
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data.plot.scatter(x = 'TotalIncome', y = 'LoanAmount', ax = ax_3)
ax_1.set_title('TotalIncome')


