# Quiz: Milestone Project — Contact Book

1. Which data structure is used to store all contacts in memory?
   - a) List of tuples
   - b) Set of dicts
   - c) Dict keyed by name with dict values
   - d) List of lists

2. What should happen if the user adds a contact with a name that already exists?
   - a) Silently overwrite
   - b) Raise an error
   - c) Ask the user if they want to overwrite
   - d) Skip the operation

3. Which dict method is safest for retrieving a contact that might not exist?
   - a) `contacts[name]`
   - b) `contacts.get(name)`
   - c) `contacts[name] if name in contacts`
   - d) `contacts[name, None]`

4. How do you delete a key from a dictionary?
   - a) `contacts.remove(name)`
   - b) `contacts.delete(name)`
   - c) `del contacts[name]`
   - d) `contacts.pop(name)` (also works)

5. What does `name in contacts` check?
   - a) If name is a value in contacts
   - b) If name is a key in contacts
   - c) If name is an item in contacts
   - d) If name is the length of contacts

6. Which loop is most appropriate for the menu-driven contact book?
   - a) `for` loop
   - b) `while True` with `break`
   - c) List comprehension
   - d) Recursion

7. What is displayed when the user chooses "View all" and there are no contacts?
   - a) An empty list
   - b) "No contacts found."
   - c) Nothing
   - d) An error

8. How do you allow the user to keep the current value during update?
   - a) Use a sentinel value
   - b) Check if input is empty string and skip assignment
   - c) Pre-fill the input with current value
   - d) Ask separately for each field

9. What is the purpose of `if __name__ == "__main__":`?
   - a) It's always required
   - b) It runs the code only when the script is executed directly
   - c) It prevents the script from running
   - d) It imports other modules

10. When searching a contact, what should you use to safely retrieve without KeyError?
    - a) `contacts[name]`
    - b) `contacts.get(name, "Not found")`
    - c) `contacts[name] if name in contacts else "Not found"`
    - d) Both b and c

**Answers:** 1-c, 2-c, 3-b, 4-d (also c works, but d is a method), 5-b, 6-b, 7-b, 8-b, 9-b, 10-d
