### Project Overview

 Determine if the instance is a crater or not a crater. 1=Crater, 0=Not Crater.
Dataset used was generated using HRSC nadir panchromatic image h0905_0000 taken by the Mars Express spacecraft. The images is located in the Xanthe Terra, centered on Nanedi Vallis and covers mostly Noachian terrain on Mars. The image had a resolution of 12.5 meters/pixel.
The images of the crater has already been converted to numpy array and is provided.


### Learnings from the project

 After completing this project, one will have a better understanding of how to build a decision tree model. In this project, we will apply the following concepts.

Train-test split, Standardize the data using MinMaxScaler , Logistic Regression, Decision Tree Modeling, Evaluation Metrics, Random Forest Algorithm, Ensemble methods - Bagging Aggregation and Voting classifier.


### Approach taken to solve the problem

 1. Data loading, splitting the data into training and test sets, Standardize the data using MinMaxScaler.
2. Predict the values after building a Machine learning model using LogisticRegression and check its roc_auc_score.
3. Predict the values after building a Machine learning model using Decision Tree and check its roc_auc_score.
4. Predict the values after building a Machine learning model using Random Forest and check its roc_auc_score. Compare the score with previous   
    models to check for improvement.
5. Apply Bagging classifier
6. Apply Voting classifier on three different ML models.



