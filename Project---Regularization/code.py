# --------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# path- variable storing file path
df = pd.read_csv(path)
df.head(5)
X = df.drop(['Price'],axis = 1)
y = df['Price']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 6)
corr = X_train.corr()
print(corr)
#Code starts here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Code starts here
regressor = LinearRegression()
regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_test)
r2 = round(r2_score(y_test,y_pred),2)
print('r2 score = ',r2)


# --------------
from sklearn.linear_model import Lasso

# Code starts here
# Code starts here
lasso = Lasso()
lasso.fit(X_train,y_train)
lasso_pred = lasso.predict(X_test)
r2_lasso = round(r2_score(y_test,lasso_pred),2)
print('r2 score = ',r2_lasso)


# --------------
from sklearn.linear_model import Ridge

# Code starts here
ridge = Ridge()
ridge.fit(X_train,y_train)
ridge_pred = ridge.predict(X_test)
r2_ridge = round(r2_score(y_test,ridge_pred),2)
print('r2 score = ',r2_ridge)


# Code ends here


# --------------
from sklearn.model_selection import cross_val_score

# Code starts here
regressor = LinearRegression()

# cross validation with LinearRegression
score = cross_val_score(regressor,X_train ,y_train,cv=10)
print(score)
mean_score = np.mean(score)
print('mean_score = ',mean_score)


# --------------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#Code starts here
model = make_pipeline(PolynomialFeatures(2), LinearRegression())
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print(y_pred)
r2_poly = r2_score(y_test,y_pred)
print(r2_poly)


