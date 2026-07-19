# Exercises: Data Cleaning & Analysis with pandas

Use the following DataFrame for exercises:

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Bob', 'Alice'],
    'Department': ['Sales', 'Sales', 'Engineering', 'Engineering', 'Sales', 'Sales', None],
    'Salary': [70000, 80000, 90000, None, 65000, 80000, 70000],
    'Join_Year': [2020, 2021, 2019, 2020, 2022, 2021, 2020]
})
```

## Exercise 1: Missing Data
Find how many null values exist in each column. Then drop rows with any null values.

## Exercise 2: Fill Missing Values
Fill missing Salary values with the mean salary.

## Exercise 3: Duplicates
Check for duplicate rows and remove them, keeping the first occurrence.

## Exercise 4: String Operations
Create a new column 'Email' by taking the Name, converting to lowercase, and appending '@company.com'.

## Exercise 5: GroupBy
Group by Department and calculate the mean and sum of Salary.

## Exercise 6: Merge
Create a second DataFrame with department budgets and merge it with the employee data.

## Challenge: Complete Data Pipeline
Given a CSV with columns Date, Product, Category, Quantity, Price, create a pipeline that:
1. Loads the data
2. Cleans: handle missing Quantity (fill with median) and drop rows with missing Price
3. Removes duplicate rows
4. Creates a 'Revenue' column
5. Groups by Category and finds total revenue
6. Creates a pivot table of total revenue by Category and Product
7. Saves the cleaned data to a new CSV
