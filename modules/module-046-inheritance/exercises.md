# Module 046: Exercises

## Exercise 1: Basic Inheritance
Define a `class Animal` with `__init__(self, name)` and a method `speak()`. Define `Dog(Animal)` and `Cat(Animal)` that override `speak()`.

## Exercise 2: Using `super()`
Define `class Vehicle` with `__init__(self, make, model)`. Define `Car(Vehicle)` that adds `doors` using `super().__init__()`.

## Exercise 3: `isinstance()` and `issubclass()`
Use the classes from Ex 1. Create instances and check their types with `isinstance()` and `issubclass()`.

## Exercise 4: Override and Extend
Define `class Employee` with `work()` returning "Working...". Define `Manager(Employee)` that overrides `work()` to return "Managing..." but also calls `super().work()`.

## Exercise 5: MRO with Multiple Inheritance
Define classes `A`, `B(A)`, `C(A)`, `D(B, C)`. Print the MRO of D and predict which method is called.

## Exercise 6: Inheriting from Built-in
Create a `class ReverseList(list)` that overrides `__getitem__` to return items in reverse order.

## Exercise 7: Hierarchical Inheritance
Define `Person` → `Student(Person)` and `Teacher(Person)`. Each should have appropriate `__init__` using `super()`.

## Exercise 8: Preventing Override
Define a `class Base` with a method that you want to prevent from being overridden (hint: don't include it in the subclass; use a non-overridden private method pattern).

## Exercise 9: Mixin Classes
Create a `class TimestampMixin` that adds `created_at` attribute in `__init__`. Use it with multiple inheritance alongside another class.

## Exercise 10: Abstract-Like Base
Define a `class Shape` where `area()` raises `NotImplementedError`. Define `Circle(Shape)` and `Rectangle(Shape)` that implement it.
