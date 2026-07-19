# Module 044: Exercises

## Exercise 1: Class Variable Counter
Define a `class Animal` with a class variable `count = 0`. Increment it in `__init__`. Create 5 animals and print the count.

## Exercise 2: Instance Variable vs Class Variable
Define a `class Employee` with class variable `company = "Inc"` and instance variable `name`. Show that each instance has its own name but shares the company.

## Exercise 3: Modifying Class Variable
Use the Employee class from Ex 2. Change `company` via the class and verify all instances see the change. Then shadow it via one instance.

## Exercise 4: Tracking Instance Data
Define a `class Student` where each instance has `name` and `grades` (instance). Add a method `add_grade(self, grade)`.

## Exercise 5: Class Variable for Defaults
Define a `class Car` with class variable `wheels = 4` and instance variables `make` and `model`. Print wheels for several cars.

## Exercise 6: Mutable Class Variable Pitfall
Define a `class Team` with a class variable `members = []`. Add members via different instances. Show the problem and fix it.

## Exercise 7: `__dict__` Inspection
Define a `class Point` with class variable `origin = (0, 0)` and instance variables `x` and `y`. Print `__dict__` for class and instance.

## Exercise 8: Class Variable for Configuration
Define a `class Database` with class variables `host = "localhost"` and `port = 5432`. Create instances that can override these.

## Exercise 9: Counting Instances per Subclass
Define `Animal`, `Dog(Animal)`, `Cat(Animal)`. Use separate class variable counts to track how many of each type exist.

## Exercise 10: Logging Attribute Changes
Define a `class Logger` where assigning to any instance attribute prints a message. Hint: use `__setattr__`.
