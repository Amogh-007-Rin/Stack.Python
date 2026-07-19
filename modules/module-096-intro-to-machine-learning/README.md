# Module 096: Introduction to Machine Learning with Python (numpy, scikit-learn)

- **Phase:** 10. Concurrency & Internals
- **Duration:** 3 hours

## Learning Objectives

- Use numpy for numerical operations (ndarray, shape, reshape)
- Understand the scikit-learn API (fit, predict, score)
- Split data into training and test sets
- Build a simple linear regression model
- Perform classification with k-nearest neighbors
- Evaluate models with accuracy, precision, recall

## Topics Covered

1. numpy basics: ndarray, shape, reshape, basic operations
2. scikit-learn overview
3. train/test split
4. Simple linear regression example
5. Classification with k-nearest neighbors
6. Evaluation metrics: accuracy, precision, recall
7. The ML pipeline: data -> train -> evaluate -> predict

## Prerequisites

Modules 000-095.

## Key Concepts

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from typing import Tuple, Any

# numpy basics
arr: np.ndarray = np.array([[1, 2], [3, 4]])
print(arr.shape, arr.reshape(4,))

# Linear regression
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model: LinearRegression = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Classification
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
```

## Resources

- numpy documentation: https://numpy.org/doc
- scikit-learn documentation: https://scikit-learn.org
- "Hands-On Machine Learning with Scikit-Learn" by Géron

## Next Module

Module 097: Packaging and Distributing Python Projects (PyPI)
