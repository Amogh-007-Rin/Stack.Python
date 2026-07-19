# Module 049: Exercises

## Exercise 1: Simple ABC
Define an ABC `Shape` with an abstract method `area()`. Create `Circle(Shape)` and `Rectangle(Shape)`.

## Exercise 2: Multiple Abstract Methods
Define an ABC `Media` with abstract methods `play()` and `stop()`. Create `Audio(Media)` and `Video(Media)`.

## Exercise 3: Cannot Instantiate ABC
Show that trying to instantiate an ABC directly raises `TypeError`. Also show that an incomplete subclass cannot be instantiated.

## Exercise 4: Abstract Properties
Define an ABC `Employee` with an abstract property `role` and abstract method `calculate_pay()`. Create concrete subclasses.

## Exercise 5: ABC with Default Implementation
Define an ABC `Logger` where `log(message)` is abstract but `info(message)` and `error(message)` call `log()` with formatted prefixes.

## Exercise 6: Register Virtual Subclass
Define an ABC `Iterable`. Register `list` and `tuple` as virtual subclasses. Use `isinstance()` to verify.

## Exercise 7: Using `collections.abc`
Use `collections.abc.Sequence` to check if your custom class qualifies as a sequence (needs `__getitem__` and `__len__`).

## Exercise 8: Abstract Class with Concrete Methods
Define an ABC `Database` with an abstract `connect()` and a concrete `execute(sql)` that calls `connect()` first.

## Exercise 9: Factory Function with ABC
Define an ABC `Animal`. Create `Dog(Animal)` and `Cat(Animal)`. Write a factory function `create_animal(animal_type, name)` that returns the right type.

## Exercise 10: Real-World Interface
Define an ABC `PaymentProcessor` with abstract methods `process_payment(amount)` and `refund(transaction_id)`. Implement `CreditCardProcessor` and `PayPalProcessor`.
