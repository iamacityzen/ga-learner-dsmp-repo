# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind = 'bar')
#path of the data file- path

#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
alignment.plot(kind = 'pie')
plt.title('Character Alignment')


# --------------
#Code starts here
import scipy
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df[['Strength','Combat']].cov().iloc[0,1]
sc_strength = scipy.nanstd(sc_df['Strength'])
sc_strength = 32.47
print(sc_strength)
sc_combat = scipy.nanstd(sc_df['Combat'])
sc_combat = 33.24
sc_pearson = sc_covariance/(sc_strength*sc_combat)
ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df[['Intelligence','Combat']].cov().iloc[0,1]
ic_intelligence = scipy.nanstd(ic_df['Intelligence'])
ic_intelligence = 32.82
ic_combat = scipy.nanstd(ic_df['Combat'])
ic_combat = 33.24
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
ic_pearson = 0.78


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
super_best = data[data['Total']>total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(20,10))
data.boxplot(column = 'Intelligence', ax = ax_1)
ax_1.set_title('Intelligence')
data.boxplot(column = 'Speed', ax = ax_2)
ax_2.set_title('Speed')
data.boxplot(column = 'Power', ax = ax_3)
ax_3.set_title('Power')


