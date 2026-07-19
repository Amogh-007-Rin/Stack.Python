# Exercises: Memory Management & Garbage Collection in CPython

## Exercise 1: Reference Counting
Create a list and assign it to multiple variables. Use `sys.getrefcount` to track the reference count changes.

## Exercise 2: Circular Reference
Create two classes `Parent` and `Child` that reference each other. Verify that they are not freed by reference counting alone.

## Exercise 3: GC Collection
Use `gc.get_objects()` to count the number of objects before and after creating many temporary objects. Force collection with `gc.collect()`.

## Exercise 4: Generational GC
Use `gc.get_count()` and `gc.get_threshold()` to observe the state of each generation. Create garbage in generation 0 and watch it age.

## Exercise 5: `__del__` Danger
Create a class with `__del__` that creates a circular reference. Show how `__del__` prevents the GC from collecting the cycle.

## Exercise 6: Weak References
Create a cache using `weakref.WeakValueDictionary` that does not prevent keys from being garbage collected.

## Challenge: Memory Leak Detector
Write a context manager that tracks object allocations and detects objects that were not freed after the context exits. Print a warning for leaked objects.
