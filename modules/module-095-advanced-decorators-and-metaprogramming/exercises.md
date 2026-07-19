# Exercises: Advanced Decorators & Metaprogramming

## Exercise 1: Decorator with Arguments
Write a `@timeout(seconds)` decorator that raises an exception if the decorated function takes longer than the specified time.

## Exercise 2: Class Decorator
Write a `@singleton` class decorator that ensures a class can only have one instance.

## Exercise 3: functools.wraps
Write a decorator that logs function calls (name, args, kwargs). Verify that `functools.wraps` preserves the original function's metadata.

## Exercise 4: Dynamic Class Creation
Use `type()` to create a class `Person` with attributes `name` and `age`, and a method `greet` that returns a greeting string.

## Exercise 5: Simple Metaclass
Write a metaclass that automatically adds a `created_at` timestamp attribute to every instance of classes that use it.

## Exercise 6: __slots__ Optimization
Create a class with 10 attributes using `__slots__` and one without. Create 100,000 instances of each and compare memory usage.

## Challenge: ORM-like Metaclass
Write a metaclass that maps class attributes to a simple in-memory database table. Support `create`, `read`, `update`, `delete` class methods.
