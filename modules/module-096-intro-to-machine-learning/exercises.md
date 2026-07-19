# Exercises: Introduction to Machine Learning with Python

## Exercise 1: numpy Array Operations
Create a 3x3 numpy array with values 1-9. Compute the sum of each row, each column, and the entire matrix.

## Exercise 2: Linear Regression
Generate synthetic data: `y = 3x + 5 + noise`. Split into train/test, fit a linear regression model, and report the R2 score.

## Exercise 3: k-NN Classification
Use the iris dataset. Split into train/test. Train a k-NN classifier with k=5. Report accuracy, precision, and recall.

## Exercise 4: Train/Test Split
Explain why splitting data is important. Try splitting without `train_test_split` using manual slicing and compare.

## Exercise 5: Model Evaluation
Train both a linear regression and a k-NN regressor on the diabetes dataset. Compare MSE and R2 scores.

## Exercise 6: Feature Scaling
Apply `StandardScaler` to the iris dataset before training k-NN. Compare accuracy with and without scaling.

## Challenge: ML Pipeline
Build a complete pipeline on the wine dataset: load data, split, scale features, train a k-NN classifier, tune `n_neighbors` (try 3, 5, 7, 9), and select the best model based on cross-validation score.
