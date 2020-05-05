### Project Overview

 Predict the Insurance claim using logistic regression. 
The dataset used contains information on the insurance claim. Each observation is different policyholder with various features like the age of the person, the gender of the policyholder, body mass index, providing an understanding of the body, number of children of the policyholder, smoking state of the policyholder and individual medical costs billed by health insurance.


### Learnings from the project

 After completing this project, one will have a better understanding of how to build a logistic regression model. In this project, following concepts will be applied

Train-test split, Correlation between the features, Logistic Regression, AUC score, and ROC AUC plot.


### Approach taken to solve the problem

 1. Data loading and splitting
2. Outlier Detection by plotting box-plot on column 'bmi'.
3. Finding Correlation between the features of training data and plot a pair plot to visualize the correlation.
4. Observe the features which highly correlated with the target variable 'insuranceclaim' by plotting count_plot for different features vs target variable.
5. Predict the insuranceclaim using logistic regression. Select the best model by cross-validation using Grid Search and check accuracy.
6. Visualize the performance of a binary classifier. Check the performance of the classifier using roc auc curve


