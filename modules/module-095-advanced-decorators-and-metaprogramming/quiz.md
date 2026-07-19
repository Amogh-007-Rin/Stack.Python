# Quiz: Advanced Decorators & Metaprogramming

## Question 1
What is the purpose of `functools.wraps` in a decorator?
- A) It makes the decorator run faster
- B) It preserves the original function's metadata (name, docstring, etc.)
- C) It wraps the arguments in a tuple
- D) It prevents the decorator from being applied multiple times

## Question 2
How do you create a decorator that accepts arguments?
- A) Add an extra level of nesting (decorator -> wrapper -> inner)
- B) Use a class instead of a function
- C) It's not possible in Python
- D) Use the `@decorator_args` syntax

## Question 3
What does `type('MyClass', (object,), {'x': 5})` do?
- A) Returns the type of MyClass
- B) Creates a new class dynamically
- C) Checks if MyClass is a type
- D) Raises an error

## Question 4
What is a metaclass?
- A) A class that inherits from multiple classes
- B) A class of a class (the class used to create classes)
- C) A class with only static methods
- D) A class that cannot be instantiated

## Question 5
What is the benefit of `__slots__`?
- A) It makes attribute access faster
- B) It reduces memory usage per instance
- C) It prevents new attribute creation
- D) All of the above

## Answer Key
1-B, 2-A, 3-B, 4-B, 5-D
