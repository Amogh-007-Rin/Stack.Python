# Exercises: Type Hints and Static Typing

All solutions must include complete type hints.

## Exercise 1: Basic Function Hints
Add type hints to a function that takes two integers and returns their sum.

## Exercise 2: Optional Parameter
Write a function `greet` that takes an optional `name: Optional[str]` and returns a greeting string.

## Exercise 3: Collection Types
Write a function `double_values` that takes a `List[int]` and returns a `List[int]` with each value doubled.

## Exercise 4: Dict and Tuple
Write a function that takes a `Dict[str, int]` and returns a `List[Tuple[str, int]]` sorted by value.

## Exercise 5: Union Type
Write a function `parse_id` that accepts `Union[int, str]` and returns an `int`. If given a string, try to convert; if given an int, return as-is.

## Exercise 6: Callable
Write a function `apply_twice` that takes a `Callable[[int], int]` and an `int`, and applies the function twice.

## Exercise 7: Generic Function
Use `TypeVar` to write a generic `first` function that returns the first element of a list.

## Challenge: Generic Stack Class
Use `Generic` to create a type-safe `Stack[T]` class with `push`, `pop`, and `is_empty` methods.
