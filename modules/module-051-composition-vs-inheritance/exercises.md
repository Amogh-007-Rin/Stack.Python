# Module 051: Composition vs Inheritance — Exercises

1. **Basic Inheritance**: Create a `Shape` base class with an `area()` method. Create `Circle` and `Rectangle` subclasses that override `area()`. Demonstrate polymorphism.

2. **Basic Composition**: Create `Author` and `Book` classes where `Book` has-an `Author` (composition). `Author` should have `name` and `nationality`. `Book` should have `title`, `year`, and `author`.

3. **Composition vs Inheritance Decision**: You need to model a `University` system with `Professor`, `Student`, and `Course`. Decide which relationships should be composition and which should be inheritance. Implement the classes.

4. **Refactor from Inheritance to Composition**: Given:
   ```python
   class Engine:
       def start(self): return "Engine running"
   
   class Car(Engine):  # Wrong: Car is-not-a Engine
       def drive(self): return f"{self.start()} — Car moving"
   ```
   Refactor to use composition. Then add a `Transmission` class and compose it into `Car` as well.

5. **UML to Code**: Translate this UML into code:
   ```
   +----------+       +----------+
   | Computer |<>-----|   CPU    |
   +----------+       +----------+
   | +powerOn |       | +process |
   +----------+       +----------+
         |
         | (inheritance)
         v
   +-------------+
   |    Laptop   |
   +-------------+
   | +batteryLife|
   +-------------+
   ```
