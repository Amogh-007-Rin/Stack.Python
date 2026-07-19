# Module 054: Enums — Exercises

1. **Basic Enum**: Create a `Weekday` enum with `MONDAY` through `SUNDAY`. Write a function `is_weekend(day: Weekday) -> bool`.

2. **auto() Values**: Create a `LogLevel` enum with `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` using `auto()`. Print each member name and value.

3. **IntEnum**: Create a `HttpStatus` IntEnum with `OK=200`, `NOT_FOUND=404`, `SERVER_ERROR=500`. Show that you can compare with integers.

4. **Enum Iteration**: Create a `Suit` enum (HEARTS, DIAMONDS, CLUBS, SPADES). Iterate over all members and print them. Check `len(Suit)`.

5. **Enums vs Constants**: Create an `OrderStatus` enum with `PENDING`, `CONFIRMED`, `SHIPPED`, `DELIVERED`. Write a function that only accepts `OrderStatus` (not arbitrary strings). Show type safety benefits.
