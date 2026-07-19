# Module 078: Introduction to Data with pandas

- **Phase:** 8. Data, Web & APIs
- **Duration:** 2.5 hours

## Learning Objectives

- Create and work with pandas Series and DataFrame
- Read data from CSV, Excel, and JSON files
- Explore data with .head(), .info(), .describe()
- Select columns and filter rows
- Perform basic calculations

## Topics Covered

1. pandas Series and DataFrame
2. Reading data (pd.read_csv, pd.read_excel, pd.read_json)
3. Basic exploration (.head, .info, .describe, .columns, .shape)
4. Selecting columns
5. Basic filtering with boolean masks
6. Simple calculations (sum, mean, min, max)

## Prerequisites

Modules 000-077.

## Key Concepts

```python
import pandas as pd

# Create DataFrame
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)

# Read CSV
df = pd.read_csv('data.csv')

# Explore
print(df.head())
print(df.info())
print(df.describe())

# Filter
adults = df[df['Age'] >= 18]
```

## Resources

- pandas documentation: https://pandas.pydata.org
- "Python for Data Analysis" by Wes McKinney
