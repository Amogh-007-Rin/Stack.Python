# Module 067: Regular Expressions — Exercises

1. **re.search**: Search for the pattern `"Python"` in the string `"I love Python programming"`. Print the match object and the matched text.

2. **re.findall**: Find all email addresses in the string `"Contact: alice@example.com and bob@test.org"` using the pattern `r"\w+@\w+\.\w+"`.

3. **re.sub**: Replace all occurrences of `"cat"` with `"dog"` in `"The cat sat on the mat, and another cat joined"`.

4. **re.split**: Split the string `"apple,banana;orange|grape"` on commas, semicolons, or pipes using a character class `[,;|]`.

5. **Groups and named groups**: From the string `"2025-06-15 14:30:00 ERROR Something went wrong"`, extract the date, time, level, and message using named groups with patterns like `(?P<name>...)`.

6. **Compiled patterns**: Use `re.compile` to create a pattern for US phone numbers `(XXX) XXX-XXXX`. Use it to search in multiple strings and extract area codes.
