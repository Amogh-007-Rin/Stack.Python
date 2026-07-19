# Module 053: Dataclasses — Exercises

1. **Basic Dataclass**: Create a `@dataclass` called `Product` with `name: str`, `price: float`, `quantity: int = 0`. Instantiate a few products and print them.

2. **field() with default_factory**: Create a `Team` dataclass with `name: str` and `members: list[str]` (use `default_factory=list`). Add a method `add_member(name: str)`.

3. **Frozen Dataclass**: Create an immutable `Coordinate` dataclass with `lat: float` and `lon: float`. Verify that attempting to set an attribute raises an error.

4. **Dataclass Inheritance**: Create a base `Employee` dataclass with `name: str` and `salary: float`. Create a `Manager` subclass that adds `bonus: float` and a computed `total_compensation` property.

5. **Comparison**: Write a `Version` dataclass with `major: int`, `minor: int`, `patch: int`. Enable ordering (use `order=True`). Sort a list of versions.
