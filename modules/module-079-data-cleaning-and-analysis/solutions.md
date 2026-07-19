# Solutions: Data Cleaning & Analysis with pandas

## Exercise 1: Missing Data
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Bob', 'Alice'],
    'Department': ['Sales', 'Sales', 'Engineering', 'Engineering', 'Sales', 'Sales', None],
    'Salary': [70000, 80000, 90000, None, 65000, 80000, 70000],
    'Join_Year': [2020, 2021, 2019, 2020, 2022, 2021, 2020]
})

print('Null counts:')
print(df.isnull().sum())

df_clean = df.dropna()
print('\\nAfter dropna:')
print(df_clean)
```

## Exercise 2: Fill Missing Values
```python
mean_salary = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(mean_salary)
print(df)
```

## Exercise 3: Duplicates
```python
print('Duplicates:', df.duplicated().sum())
df = df.drop_duplicates(keep='first')
print('After dedup:', df.shape)
```

## Exercise 4: String Operations
```python
df['Email'] = df['Name'].str.lower() + '@company.com'
print(df[['Name', 'Email']])
```

## Exercise 5: GroupBy
```python
grouped = df.groupby('Department')['Salary'].agg(['mean', 'sum', 'count'])
print(grouped)
```

## Exercise 6: Merge
```python
dept_budgets = pd.DataFrame({
    'Department': ['Sales', 'Engineering'],
    'Budget': [500000, 800000]
})

merged = pd.merge(df, dept_budgets, on='Department', how='left')
print(merged)
```

## Challenge: Complete Data Pipeline
```python
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03'],
    'Product': ['A', 'B', 'A', 'B', 'A'],
    'Category': ['Electronics', 'Books', 'Electronics', 'Books', 'Electronics'],
    'Quantity': [10, 5, None, 3, 8],
    'Price': [20.0, 15.0, 25.0, None, 20.0]
})

# 1. Fill missing Quantity with median
data['Quantity'] = data['Quantity'].fillna(data['Quantity'].median())

# 2. Drop rows with missing Price
data = data.dropna(subset=['Price'])

# 3. Remove duplicates
data = data.drop_duplicates()

# 4. Revenue column
data['Revenue'] = data['Quantity'] * data['Price']

# 5. Group by Category
category_revenue = data.groupby('Category')['Revenue'].sum()
print('Category revenue:')
print(category_revenue)

# 6. Pivot table
pivot = pd.pivot_table(
    data,
    values='Revenue',
    index='Category',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)
print('\\nPivot table:')
print(pivot)

# 7. Save cleaned data
data.to_csv('cleaned_data.csv', index=False)
```
