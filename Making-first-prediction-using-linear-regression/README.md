### Project Overview

 You are a die hard Lego enthusiast wishing to collect as many board sets as you can. But before that you wish to be able to predict the price of a new lego product before its price is revealed so that you can budget it from your revenue. Since (luckily!), you are a data scientist in the making, you wished to solve this problem yourself. This dataset contains information on lego sets scraped from lego.com. Each observation is a different lego set with various features like how many pieces in the set, rating for the set, number of reviews per set etc. Your aim is to build a linear regression model to predict the price of a set.


### Learnings from the project

 After completing this project, we will have the better understanding of how to build a linear regression model. In this project, we will apply the following concepts.

Train-test split
Correlation between the features
Linear Regression
MSE andR^2-Evaluation Metrics


### Approach taken to solve the problem

 The first step is to load the dataset and see how it looks like. Additionally, split it into the train and test Plot scatter plot for different features vs target variable - list_price.,this tells us which features are highly correlated with the target variable list_price and help us predict it better.If two features are correlated and with a value greater than 0.75, remove one of them. Used linear regression to predict the price. Checked the model accuracy using r^2 score and mse. Finally calculated the cost function and visualised it.


### Challenges faced

 Understanding the scatter plot for identifying which features would be a good predictor for estimating list_price. I overcomed it by understanding scatter plot in details.


