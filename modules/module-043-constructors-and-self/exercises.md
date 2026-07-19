# Module 043: Exercises

## Exercise 1: Parameterized Constructor
Define a `class Book` with `__init__(self, title, author, year)`. Create an instance and print its attributes.

## Exercise 2: Default Values
Define a `class Timer` with `__init__(self, duration=10, unit="seconds")`. Create timers with 0, 1, and 2 arguments.

## Exercise 3: Mutable Default Trap
Create a `class Team` with `__init__(self, members=[])` and show how adding to one instance's members affects another. Then fix it.

## Exercise 4: Constructor Logic
Define a `class Rectangle` where `__init__` accepts `width` and `height`, and auto-calculates `area` as an attribute if not provided.

## Exercise 5: Class Without `__init__`
Define a class `Point` with no `__init__`. Create an instance and manually add `x` and `y` attributes.

## Exercise 6: Implicit Self
Define a `class Example` with a method that prints `id(self)`. Create an instance and call the method. Also call it explicitly via the class.

## Exercise 7: Smart Constructor
Define a `class Email` where `__init__` takes an email string and automatically extracts `username` and `domain`.

## Exercise 8: Validation in Constructor
Define a `class Person` where `__init__` validates that `age` is between 0 and 150, raising `ValueError` otherwise.

## Exercise 9: Keyword Arguments
Define a `class Config` where `__init__` accepts `**kwargs` and sets each key as an attribute.

## Exercise 10: Preventing Attribute Addition
Define a `class FixedPoint` with `__slots__ = ['x', 'y']`. Show that adding a `z` attribute raises `AttributeError`.
