# Module 059: Working with Files: CSV — Exercises

1. **csv.writer**: Write a list of lists `[["Name", "Age"], ["Alice", 30], ["Bob", 25]]` to `people.csv` using `csv.writer`. Verify by reading it back.

2. **csv.DictWriter**: Write the same data using `csv.DictWriter` with fieldnames `["Name", "Age"]`.

3. **csv.reader**: Read `people.csv` from exercise 1 and convert each row to a dictionary manually (first row is header).

4. **csv.DictReader**: Read `people.csv` using `csv.DictReader` and print each row. Compute the average age.

5. **Custom delimiter**: Write a TSV (tab-separated) file using `delimiter="\t"`. Read it back with the same delimiter.

6. **CSV with quoting**: Write a CSV file where a field contains a comma (e.g., "Smith, John"). Use `csv.QUOTE_ALL` to ensure proper quoting. Read it back.
