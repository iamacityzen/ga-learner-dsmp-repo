# --------------
import pandas as pd
from sklearn import preprocessing

#path : File path

# Code starts here
dataset = pd.read_csv(path)
dataset.drop(['Id'],axis = 1,inplace = True)

# read the dataset



# look at the first five columns


# Check if there's any column which is not useful and remove it like the column id


# check the statistical description



# --------------
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt

#names of all the attributes 
cols = dataset.columns

#number of attributes (exclude target)
size = len(cols) - 1

#x-axis has target attribute to distinguish between classes
x = cols[size]

#y-axis shows values of an attribute
y = cols[0:size]

#Plot violin for all attributes
for i in range(0,size):
    sns.violinplot(data = dataset,x=x,y = [i])
    plt.show()



# --------------
import numpy
upper_threshold = 0.5
lower_threshold = -0.5


# Code Starts Here
subset_train = dataset.iloc[:, :10]
data_corr = subset_train.corr()
correlation = data_corr.unstack().sort_values(kind='quicksort')
corr_var_list = correlation[((correlation>upper_threshold)|(correlation<lower_threshold)) & (correlation!=1)]

# Code ends here




# --------------
#Import libraries 
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler

# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)
r,c = dataset.shape
X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,-1]

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X,Y,test_size = 0.2, random_state = 0)
scaler = StandardScaler()
X_train_temp = StandardScaler().fit_transform(X_train.iloc[:,:10])
X_test_temp = StandardScaler().fit_transform(X_test.iloc[:,:10])


# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.
X_train1 = numpy.concatenate((X_train_temp,X_train.iloc[:,10:c-1]),axis = 1)
X_test1 = numpy.concatenate((X_test_temp,X_test.iloc[:,10:c-1]),axis = 1)


#Standardized
#Apply transform only for continuous data
scaled_features_train_df = pd.DataFrame(X_train1,index = X_train.index,columns = X_train.columns)

#Concatenate scaled continuous data and categorical
scaled_features_test_df = pd.DataFrame(X_test1,index = X_test.index,columns = X_test.columns)



# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif


# Write your solution here:
skb = SelectPercentile(score_func=f_classif ,percentile=90)
predictors = skb.fit_transform(X_train1,Y_train)
scores = list(skb.scores_)
Features = scaled_features_train_df.columns
dataframe = pd.DataFrame({'Features':Features,'Scores' :scores})
dataframe = dataframe.sort_values(by = 'Scores' ,ascending = False)
top_k_predictors = list(dataframe['Features'][:predictors.shape[1]])





# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score
clf = OneVsRestClassifier(LogisticRegression())
clf1 = OneVsRestClassifier(LogisticRegression())
model_fit_all_features = clf1.fit(X_train,Y_train)
predictions_all_features = model_fit_all_features.predict(X_test)
score_all_features = accuracy_score(Y_test, predictions_all_features)
model_fit_top_features = clf.fit(scaled_features_train_df[top_k_predictors], Y_train)
precision_top_features = model_fit_top_features.predict(scaled_features_test_df[top_k_predictors])
score_top_features = 0.6755952380952381


