# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
df.shape
p_a = df[df['fico']>700].shape[0]/df.shape[0]
p_b = df[df['purpose'] == 'debt_consolidation'].shape[0]/df.shape[0]
df1 = df[df['purpose'] == 'debt_consolidation']
(p_a and p_b)/p_b
p_a_b = (p_b and p_a)/p_a
result = p_a_b == p_b
# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan'] =='Yes'].shape[0]/df.shape[0]
prob_cs = df[df['credit.policy'] =='Yes'].shape[0]/df.shape[0]
new_df = df[df['paid.back.loan'] =='Yes']
prob_pd_cs = new_df[new_df['credit.policy'] =='Yes'].shape[0]/new_df.shape[0]
bayes = (prob_pd_cs * prob_lp)/prob_cs
print(bayes)


# code ends here


# --------------
# code starts here
df.purpose.value_counts(normalize=True).plot(kind = 'bar')
df1 = df[df['paid.back.loan'] =='No']
df1.purpose.value_counts(normalize=True).plot(kind = 'bar')
# code ends here


# --------------
# code starts here
inst_mean = df['installment'].mean()
inst_median = df['installment'].median()


# code ends here


