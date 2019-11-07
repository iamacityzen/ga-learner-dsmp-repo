# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record= [[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
print(type(data))
new_record = np.array(new_record)
census = np.concatenate((data,new_record),axis = 0) 



# --------------
#Code starts here
age = census[:,[0]]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)


# --------------
#Code starts here
race = census[:,2]
print(race)
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
len_0  = len(race_0)
print(len_0)
len_1 = len(race_1)
print(len_1)
len_2 = len(race_2)
print(len_2)
len_3 = len(race_3)
print(len_3)
len_4 = len(race_4)
print(len_4)
lengths = [len_0,len_1,len_2,len_3,len_4]

minority_race = lengths.index(min(lengths))


# --------------
#Code starts here
senior_citizens =census[census[:,0] > 60]
print(senior_citizens)
working_hours_sum=senior_citizens.sum(axis=0)[6]
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]
avg_pay_high = high.mean(axis = 0)[7]
avg_pay_low = low.mean(axis = 0)[7]
avg_pay_high
avg_pay_low
np.array_equal(avg_pay_high,avg_pay_low)

