# Module 061: Working with JSON — Exercises

1. **json.dumps**: Create a dictionary `{"name": "Alice", "age": 30, "city": "New York"}` and serialize it to a JSON string using `json.dumps`. Print the result.

2. **json.dump**: Write the same dictionary to a file called `person.json` using `json.dump`. Verify by reading the file back as text.

3. **json.loads**: Parse the JSON string `'{"product": "Laptop", "price": 1200.50, "in_stock": true}'` using `json.loads`. Access and print the `price` field.

4. **json.load**: Read `person.json` from exercise 2 using `json.load` and print the resulting dictionary. Modify the age to 31 and write it back.

5. **Pretty-printing**: Create a nested dictionary with 3+ levels. Serialize it with `json.dumps` using `indent=2` and `sort_keys=True`. Print both the compact and pretty versions.

6. **Custom serialization**: Create a class `Person` with attributes `name` (str) and `birth_date` (datetime.date). Implement a custom `JSONEncoder` subclass that serializes `Person` objects to `{"name": ..., "birth_date": "YYYY-MM-DD"}`. Demonstrate serializing a list of `Person` instances.
