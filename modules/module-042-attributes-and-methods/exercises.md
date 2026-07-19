# Module 042: Exercises

## Exercise 1: Basic Attributes
Define a `class Product` with `__init__(self, name, price)` and a method `display()` that prints the name and price.

## Exercise 2: Method with Return
Define a `class Square` with `__init__(self, side)` and a method `area()` that returns the area.

## Exercise 3: Dynamic Attributes
Create an `class Empty` with no `__init__`. Create an instance, add attributes `x = 10` and `y = 20` dynamically, then print them.

## Exercise 4: BankAccount Methods
Define `class BankAccount` with `deposit(amount)` and `withdraw(amount)`. Include a check that prevents withdrawing more than the balance.

## Exercise 5: Student GPA
Define `class Student` with `__init__(self, name)` and a method `add_grade(self, grade)`. Include a method `gpa()` that returns the average.

## Exercise 6: Method vs Function
Create a function `greet(name)` and a class `Person` with a method `greet(self)`. Show how they are called differently.

## Exercise 7: Attribute Count
Define a `class Item` with a class attribute `count = 0`. In `__init__`, increment `count`. Create several items and print the total.

## Exercise 8: Default Attributes
Define a `class Config` with `__init__(self, host="localhost", port=8080)`. Create instances with and without arguments.

## Exercise 9: Chaining Methods
Define a `class Counter` with methods `increment()` and `decrement()`. Make them return `self` so calls can be chained: `c.increment().increment().get_value()`.

## Exercise 10: Validate Attributes
Define a `class Person` with `set_name(self, name)` that validates the name is a non-empty string, and `get_name(self)` to retrieve it.
