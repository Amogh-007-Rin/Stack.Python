# Module 032: Exercises

## Exercise 1: Default Parameter
Write a function `repeat(text, times=2)` that returns the text repeated `times` times.

## Exercise 2: Keyword Arguments
Call a function `introduce(name, age)` using keyword arguments in a different order.

## Exercise 3: *args Sum
Write a function `product(*args)` that returns the product of all numbers passed.

## Exercise 4: **kwargs
Write a function `show_settings(**kwargs)` that prints each key-value pair on a new line.

## Exercise 5: Combined
Write a function `build_url(base, *paths, **params)` that builds a URL from base, paths, and query params.

## Exercise 6: Unpack List
Write a function `multiply(a, b, c)` and call it by unpacking `[2, 3, 4]`.

## Exercise 7: Unpack Dict
Write a function `display(title, year, rating)` and call it by unpacking a dict.

## Exercise 8: Mutable Default Trap
What is the output of this code? Why?
```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))
print(add_item("b"))
```

## Exercise 9: Argument Order
Is this function definition valid? Why or why not?
```python
def func(*args, default=5):
    pass
```

## Exercise 10: Mixed Arguments
Write a function `log_message(level, *messages, **metadata)` that prints each message with level and metadata.
