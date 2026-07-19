# Module 048: Exercises

## Exercise 1: `__str__` and `__repr__`
Define a `class Person` with `name` and `age`. Implement `__repr__` and `__str__`. Print using `repr()` and `str()`.

## Exercise 2: `__eq__` and `__hash__`
Define a `class Point` with `x` and `y`. Implement `__eq__` (based on both coordinates) and `__hash__`. Test with a set.

## Exercise 3: `__len__` and `__getitem__`
Create a `class Team` that wraps a list of members. Implement `__len__` and `__getitem__` so `len(team)` and `team[0]` work.

## Exercise 4: `__contains__`
Extend the Team class from Ex 3 with `__contains__` so `"Alice" in team` works.

## Exercise 5: `__call__`
Create a `class Power` where `__init__(self, exp)` stores an exponent, and `__call__(self, base)` returns `base ** exp`.

## Exercise 6: `__bool__`
Create a `class Inventory` with `__bool__` that returns `True` if the inventory has items.

## Exercise 7: `__add__`
Define a `class Money` with `amount` and `currency`. Implement `__add__` that adds amounts if currencies match.

## Exercise 8: `__repr__` for Debugging
Create a `class Config` where `__repr__` returns a string showing all attributes in a format that could recreate the object.

## Exercise 9: Complete Collection Interface
Define a `class Deck` representing a deck of cards. Implement `__len__`, `__getitem__`, `__contains__`, `__iter__`.

## Exercise 10: `__str__` vs `__repr__` in Practice
Define a `class Date` with year, month, day. `__repr__` should return `Date(2024, 1, 15)` and `__str__` should return `2024-01-15`.
