# Exercises: Introduction to Data with pandas

Use this sample data for exercises:

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['NYC', 'LA', 'Chicago', 'NYC', 'LA'],
    'Salary': [70000, 80000, 90000, 75000, 65000]
}
df = pd.DataFrame(data)
```

## Exercise 1: DataFrame Basics
Print the first 3 rows, column names, shape, and summary statistics.

## Exercise 2: Column Selection
Select the 'Name' and 'Salary' columns. Then select the 'Age' column as a Series.

## Exercise 3: Filtering
Find all rows where Salary > 75000. Then find NYC residents only.

## Exercise 4: Multiple Conditions
Find rows where Age > 25 AND City == 'LA'.

## Exercise 5: Calculations
Calculate the mean, min, and max of the Salary column.

## Exercise 6: Read from CSV
Create a CSV string and use `pd.read_csv()` to load it into a DataFrame.

## Challenge: Analysis Pipeline
Given a CSV of sales data (columns: Date, Product, Quantity, Price), write a pipeline that:
1. Reads the CSV
2. Shows basic info
3. Filters for Quantity > 0
4. Adds a 'Total' column (Quantity * Price)
5. Shows total sales per product
