# Module 079: Data Cleaning & Analysis with pandas

- **Phase:** 8. Data, Web & APIs
- **Duration:** 2.5 hours

## Learning Objectives

- Handle missing data with dropna, fillna, and isnull
- Remove duplicate rows
- Use string operations with .str accessor
- Group data with groupby and aggregate
- Merge and join DataFrames
- Create pivot tables

## Topics Covered

1. Missing data: dropna, fillna, isnull
2. Duplicate removal (drop_duplicates)
3. String operations (.str accessor)
4. Groupby operations
5. Aggregation (sum, mean, count, etc.)
6. Merging and joining DataFrames
7. Pivot tables

## Prerequisites

Modules 000-078.

## Key Concepts

```python
import pandas as pd

# Handle missing data
df.dropna()
df.fillna(0)
df['col'].isnull().sum()

# Groupby aggregation
df.groupby('Category')['Value'].mean()

# Merge
pd.merge(df1, df2, on='key')

# Pivot table
pd.pivot_table(df, values='Sales', index='Region', columns='Year')
```

## Resources

- pandas documentation: Working with missing data
- pandas documentation: Merge, join, concatenate
- pandas documentation: Group by
