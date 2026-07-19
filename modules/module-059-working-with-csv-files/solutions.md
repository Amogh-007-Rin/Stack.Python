# Module 059: Working with Files: CSV — Solutions

```python
import csv
import os


# 1. csv.writer
data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open("people.csv", "r", newline="", encoding="utf-8") as f:
    print(f.read())

# 2. csv.DictWriter
with open("people_dict.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["Name", "Age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Alice", "Age": 30})
    writer.writerow({"Name": "Bob", "Age": 25})

# 3. Manual conversion from reader
with open("people.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows: list[dict] = []
    for row in reader:
        rows.append({header[i]: row[i] for i in range(len(header))})
print(rows)

# 4. DictReader with average
with open("people.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    ages = [int(row["Age"]) for row in reader]
    print(f"Average age: {sum(ages) / len(ages):.1f}")

# 5. Custom delimiter (TSV)
tsv_data = [["Name", "City"], ["Alice", "New York"], ["Bob", "Los Angeles"]]
with open("data.tsv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerows(tsv_data)

with open("data.tsv", "r", newline="", encoding="utf-8") as f:
    for row in csv.reader(f, delimiter="\t"):
        print(row)

# 6. CSV with quoting
with open("quoted.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(["ID", "Name"])
    writer.writerow([1, "Smith, John"])

with open("quoted.csv", "r", newline="", encoding="utf-8") as f:
    print(f.read())

# Cleanup
for fname in ["people.csv", "people_dict.csv", "data.tsv", "quoted.csv"]:
    os.remove(fname)
```
