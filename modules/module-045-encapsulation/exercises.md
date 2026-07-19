# Module 045: Exercises

## Exercise 1: Protected Attribute
Define a `class Employee` with a protected attribute `_salary`. Add a method `get_salary()` that returns it.

## Exercise 2: Name Mangling
Define a `class Secret` with a private attribute `__secret`. Try accessing it directly, then via the mangled name.

## Exercise 3: Getter and Setter
Define a `class Temperature` with a private attribute `__celsius`. Add `get_celsius()` and `set_celsius()` with validation.

## Exercise 4: Validation in Setter
Define a `class Person` where `set_age(age)` validates age is between 0 and 150.

## Exercise 5: Read-Only Attribute
Define a `class Circle` where `__radius` is set in `__init__`, and `get_radius()` returns it but there's no setter.

## Exercise 6: Property-like Interface
Define a `class BankAccount` with `get_balance()`, `deposit()`, and `withdraw()`. Ensure balance cannot be directly modified.

## Exercise 7: Encapsulation with Calculation
Define a `class Rectangle` where `__width` and `__height` are private, and `get_area()` computes the area.

## Exercise 8: Name Mangling in Inheritance
Define a class `Parent` with `__value` and a `get_value()` method. Define `Child(Parent)` that tries to override `__value`. Show how mangling prevents collision.

## Exercise 9: Logging Setter
Define a `class Logger` where setting any attribute through a setter logs the change.

## Exercise 10: Full Encapsulation
Define a `class Student` with private attributes `__name` and `__grades`. Provide getters and a method `add_grade(grade)`.
