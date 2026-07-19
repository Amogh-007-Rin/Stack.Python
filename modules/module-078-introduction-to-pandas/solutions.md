# Solutions: Introduction to Data with pandas

## Exercise 1: DataFrame Basics
```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['NYC', 'LA', 'Chicago', 'NYC', 'LA'],
    'Salary': [70000, 80000, 90000, 75000, 65000]
}
df = pd.DataFrame(data)

print('Head:')
print(df.head(3))
print('\nColumns:', df.columns.tolist())
print('Shape:', df.shape)
print('\nDescribe:')
print(df.describe())
```

## Exercise 2: Column Selection
```python
names_salaries = df[['Name', 'Salary']]
print(names_salaries)

ages = df['Age']
print(type(ages))
print(ages)
```

## Exercise 3: Filtering
```python
high_salary = df[df['Salary'] > 75000]
print('High salary:')
print(high_salary)

nyc = df[df['City'] == 'NYC']
print('NYC residents:')
print(nyc)
```

## Exercise 4: Multiple Conditions
```python
result = df[(df['Age'] > 25) & (df['City'] == 'LA')]
print('Age > 25 and LA:')
print(result)
```

## Exercise 5: Calculations
```python
print('Mean salary:', df['Salary'].mean())
print('Min salary:', df['Salary'].min())
print('Max salary:', df['Salary'].max())
```

## Exercise 6: Read from CSV
```python
import pandas as pd
from io import StringIO

csv_data = """Name,Age,City,Salary
Alice,25,NYC,70000
Bob,30,LA,80000
Charlie,35,Chicago,90000
"""

df = pd.read_csv(StringIO(csv_data))
print(df)
```

## Challenge: Analysis Pipeline
```python
import pandas as pd
from io import StringIO

csv_data = """Date,Product,Quantity,Price
2024-01-01,Widget A,10,5.00
2024-01-01,Widget B,5,15.00
2024-01-02,Widget A,0,5.00
2024-01-02,Widget B,8,15.00
"""

df = pd.read_csv(StringIO(csv_data))
print('Info:')
print(df.info())

df = df[df['Quantity'] > 0]
df['Total'] = df['Quantity'] * df['Price']
print('\nWith totals:')
print(df)

product_totals = df.groupby('Product')['Total'].sum()
print('\nTotal sales per product:')
print(product_totals)
```
