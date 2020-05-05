# --------------
#Importing header files

import pandas as pd
from sklearn.model_selection import train_test_split


# Code starts here
data = pd.read_csv(path)
X = data.drop(['customer.id','paid.back.loan'], axis= 1)
y = data['paid.back.loan']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3 , random_state = 0)


# Code ends here


# --------------
#Importing header files
import matplotlib.pyplot as plt

# Code starts here
fully_paid = y_train.value_counts()



# Code ends here


# --------------
#Importing header files
import numpy as np
from sklearn.preprocessing import LabelEncoder


# Code starts here
X_train['int.rate'] = (X_train['int.rate'].str.replace('%', '').astype(float))/100
X_test['int.rate'] = (X_test['int.rate'].str.replace('%', '').astype(float))/100
cat_df = X_train.select_dtypes(include = ['object'])
num_df = X_train.select_dtypes(exclude = ['object'])
# Code ends here


# --------------
#Importing header files
import seaborn as sns


# Code starts here
cols = num_df.columns
# Code ends here


# --------------
# Code starts here
cols = cat_df.columns


# Code ends here


# --------------
#Importing header files
from sklearn.tree import DecisionTreeClassifier

# Code starts here
for col in cat_df.columns:
    X_train.fillna('NA')
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col])
for col in cat_df.columns:
    X_test.fillna('NA')
    le = LabelEncoder()
    X_test[col] = le.fit_transform(X_test[col])
le = LabelEncoder()
y_test = le.fit_transform(y_test)
y_train = le.fit_transform(y_train)
model = DecisionTreeClassifier(random_state = 0)
model.fit(X_train,y_train)
from sklearn.metrics import accuracy_score
test_pred = model.predict(X_test)
acc = accuracy_score(y_test,test_pred)

# Code ends here


# --------------
#Importing header files
from sklearn.model_selection import GridSearchCV

#Parameter grid
parameter_grid = {'max_depth': np.arange(3,10), 'min_samples_leaf': range(10,50,10)}

# Code starts here
model_2 = DecisionTreeClassifier(random_state = 0)
p_tree = GridSearchCV(estimator = model_2, param_grid = parameter_grid, cv = 5)
p_tree.fit(X_train,y_train)
test_pred  = p_tree.predict(X_test)
from sklearn.metrics import accuracy_score
acc_2 = accuracy_score(y_test,test_pred)


# Code ends here


# --------------
#Importing header files

from io import StringIO
from sklearn.tree import export_graphviz
from sklearn import tree
from sklearn import metrics
from IPython.display import Image
import pydotplus

# Code starts here
dot_data = tree.export_graphviz(decision_tree=p_tree.best_estimator_, out_file=None, feature_names=X.columns, filled = True ,class_names=['loan_paid_back_yes','loan_paid_back_no'])
graph_big = pydotplus.graph_from_dot_data(dot_data)
Image(graph_big.create_png())

# show graph - do not delete/modify the code below this line
img_path = user_data_dir+'/file.png'
graph_big.write_png(img_path)

plt.figure(figsize=(20,15))
plt.imshow(plt.imread(img_path))
plt.axis('off')
plt.show() 

# Code ends here


