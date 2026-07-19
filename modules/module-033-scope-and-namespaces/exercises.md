# Module 033: Exercises

## Exercise 1: Local vs Global
Predict the output:
```python
x = 5
def func():
    x = 10
    print(x)
func()
print(x)
```

## Exercise 2: Global Keyword
Write a function `reset_counter()` that uses `global` to set a global `counter` to 0.

## Exercise 3: Nonlocal
Write an outer function that creates a list, an inner function that appends to it using `nonlocal`.

## Exercise 4: Shadowing
Create a global variable `name = "Python"` and a function that shadows it.

## Exercise 5: LEGB Trace
Given this code, which scope does Python find `value` in?
```python
value = 10
def outer():
    value = 20
    def inner():
        print(value)
    inner()
outer()
```

## Exercise 6: Without Global
What happens if you try to modify a global variable inside a function without the `global` keyword?

## Exercise 7: Nested Functions
Write a function `make_counter()` that uses `nonlocal` to create a counter that increments each call.

## Exercise 8: Built-in Shadowing
What happens if you create a variable called `print`?

## Exercise 9: Global Constant
Write a function that reads a global constant `PI = 3.14159` and returns the area of a circle given radius.

## Exercise 10: Multiple Enclosing
Create three levels of nested functions. Use `nonlocal` at each level.
