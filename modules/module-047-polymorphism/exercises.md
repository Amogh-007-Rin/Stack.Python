# Module 047: Exercises

## Exercise 1: Polymorphic Function
Define classes `Cat`, `Dog`, and `Duck`, each with a `sound()` method. Write a function `make_sounds(animals)` that calls `sound()` on each.

## Exercise 2: Duck Typing
Define `class Car` with `drive()` and `class Boat` with `drive()`. Write a `travel(vehicle)` function that calls `drive()`.

## Exercise 3: Operator Polymorphism
Use `len()` on a string, list, tuple, dict, and set. Show the output for each.

## Exercise 4: Polymorphism with Inheritance
Define `class Shape` with `area()`. Define `Circle(Shape)` and `Square(Shape)`. Write code that works with any Shape.

## Exercise 5: Protocol-Based Polymorphism
Create a `class MyCollection` that implements `__len__` and `__getitem__`. Make it work with `len()` and indexing.

## Exercise 6: Polymorphic `+` Operator
Create classes `Vector` and `Point` that each implement `__add__` to support the `+` operator.

## Exercise 7: Duck Typing with Multiple Methods
Define two unrelated classes `Printer` and `Screen`, each with a `display(text)` method. Write a function that uses any object with `display()`.

## Exercise 8: `isinstance()` Check
Write code that checks if objects are instances of built-in types (str, int, list) and handles them differently.

## Exercise 9: Polymorphic Iterator
Create a `class Fibonacci` that implements `__iter__` and `__next__`. Use it in a `for` loop — this is protocol-based polymorphism.

## Exercise 10: Real-World Polymorphism
Define `class PDFReport` and `class CSVReport`, each with `generate(data)` that produces different output. Write a `generate_report(report, data)` function.
