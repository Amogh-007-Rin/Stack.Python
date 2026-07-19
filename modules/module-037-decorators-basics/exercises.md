# Module 037: Exercises

## Exercise 1: Simple Decorator
Write a decorator `@announce` that prints "Starting..." before the function and "Done!" after.

## Exercise 2: Timing Decorator
Write a decorator `@timer` that prints how long a function took in milliseconds.

## Exercise 3: Double Decorator
Apply two decorators to one function: `@uppercase` (converts return to uppercase) and `@exclaim` (adds "!").

## Exercise 4: @wraps
Create a decorator without `@wraps` and verify `__name__` is lost. Then add `@wraps`.

## Exercise 5: Return Value Modifier
Write a decorator that doubles the return value of a function.

## Exercise 6: Argument Validator
Write a decorator `@positive` that raises ValueError if any argument is negative.

## Exercise 7: Cache Decorator
Write a decorator `@cache` that stores results of previous calls and returns cached results for repeated arguments.

## Exercise 8: Decorator with Parameters
Write a decorator `@repeat(n)` that calls a function n times.

## Exercise 9: Logging Decorator
Write a decorator that logs the function name, arguments, and return value to a file.

## Exercise 10: Stacking Order
What is the output?
```python
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def hello():
    return "Hello"
print(hello())
```
