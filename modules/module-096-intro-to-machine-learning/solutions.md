# Solutions: Introduction to Machine Learning with Python

## Exercise 1: numpy Array Operations
```python
import numpy as np

arr: np.ndarray = np.arange(1, 10).reshape(3, 3)
print(f"Array:\n{arr}")
print(f"Row sums: {arr.sum(axis=1)}")
print(f"Column sums: {arr.sum(axis=0)}")
print(f"Total sum: {arr.sum()}")
```

## Exercise 2: Linear Regression
```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

np.random.seed(42)
X: np.ndarray = np.random.rand(100, 1) * 10
y: np.ndarray = 3 * X.flatten() + 5 + np.random.randn(100) * 0.5

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model: LinearRegression = LinearRegression()
model.fit(X_train, y_train)

print(f"Coefficient: {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"R2 Score: {r2_score(y_test, model.predict(X_test)):.4f}")
```

## Exercise 3: k-NN Classification
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred, average='weighted'):.4f}")
```

## Exercise 4: Train/Test Split
```python
import numpy as np
from sklearn.model_selection import train_test_split

# Manual split
X: np.ndarray = np.random.rand(100, 1)
y: np.ndarray = np.random.rand(100)
split_idx: int = int(0.8 * len(X))

X_train_manual: np.ndarray = X[:split_idx]
X_test_manual: np.ndarray = X[split_idx:]
y_train_manual: np.ndarray = y[:split_idx]
y_test_manual: np.ndarray = y[split_idx:]

# sklearn split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Manual split: {len(X_train_manual)} train, {len(X_test_manual)} test")
print(f"sklearn split: {len(X_train)} train, {len(X_test)} test")
```

## Exercise 5: Model Evaluation
```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

data = load_diabetes()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
print(f"Linear Regression - MSE: {mean_squared_error(y_test, y_pred_lr):.2f}, "
      f"R2: {r2_score(y_test, y_pred_lr):.4f}")

knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
print(f"k-NN Regressor  - MSE: {mean_squared_error(y_test, y_pred_knn):.2f}, "
      f"R2: {r2_score(y_test, y_pred_knn):.4f}")
```

## Exercise 6: Feature Scaling
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Without scaling
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
acc_no_scale: float = accuracy_score(y_test, knn.predict(X_test))
print(f"Accuracy without scaling: {acc_no_scale:.4f}")

# With scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_scaled = KNeighborsClassifier(n_neighbors=5)
knn_scaled.fit(X_train_scaled, y_train)
acc_scaled: float = accuracy_score(y_test, knn_scaled.predict(X_test_scaled))
print(f"Accuracy with scaling:    {acc_scaled:.4f}")
```

## Challenge: ML Pipeline
```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
import numpy as np
from typing import Dict, Any

data = load_wine()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

best_score: float = 0
best_k: int = 0
results: Dict[int, float] = {}

for k in [3, 5, 7, 9]:
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier(n_neighbors=k)),
    ])

    scores = cross_val_score(pipeline, X_train, y_train, cv=5)
    mean_score: float = scores.mean()
    results[k] = mean_score
    print(f"k={k}: CV accuracy = {mean_score:.4f}")

    if mean_score > best_score:
        best_score = mean_score
        best_k = k

print(f"\nBest k: {best_k} (CV accuracy: {best_score:.4f})")

final_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=best_k)),
])
final_pipeline.fit(X_train, y_train)
test_score: float = final_pipeline.score(X_test, y_test)
print(f"Test accuracy: {test_score:.4f}")
```
