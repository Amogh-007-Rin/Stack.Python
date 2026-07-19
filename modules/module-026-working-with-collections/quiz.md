# Quiz: Working with Collections

1. What does `zip([1, 2, 3], ["a", "b", "c"])` return?
   - a) `[(1, "a"), (2, "b"), (3, "c")]`
   - b) `[(1, "a"), (2, "b")]`
   - c) A zip object (iterator)
   - d) `{"a": 1, "b": 2, "c": 3}`

2. What happens if zip gets iterables of different lengths?
   - a) It raises an error
   - b) It stops at the shortest iterable
   - c) It pads shorter ones with None
   - d) It stops at the longest iterable

3. What does `enumerate(["a", "b", "c"])` produce?
   - a) `{0: "a", 1: "b", 2: "c"}`
   - b) `[(0, "a"), (1, "b"), (2, "c")]`
   - c) An enumerate object yielding `(index, value)` tuples
   - d) `["0: a", "1: b", "2: c"]`

4. How do you start enumerate at index 1?
   - a) `enumerate(lst, 1)`
   - b) `enumerate(lst, start=1)`
   - c) Both a and b
   - d) `enumerate(lst, offset=1)`

5. Which itertools function generates an infinite arithmetic sequence?
   - a) `cycle()`
   - b) `count()`
   - c) `repeat()`
   - d) `chain()`

6. Which itertools function repeats a single value infinitely?
   - a) `cycle()`
   - b) `count()`
   - c) `repeat()`
   - d) `chain()`

7. Which itertools function combines multiple iterables end-to-end?
   - a) `zip()`
   - b) `chain()`
   - c) `product()`
   - d) `combine()`

8. What is the difference between `permutations` and `combinations`?
   - a) Permutations care about order; combinations do not
   - b) Combinations care about order; permutations do not
   - c) They are the same
   - d) Permutations allow repeats; combinations do not

9. How many 2-element permutations of `["a", "b", "c"]` exist?
   - a) 3
   - b) 6
   - c) 9
   - d) 2

10. What does `zip(*[("x", 1), ("y", 2)])` do?
    - a) Transposes the list of tuples into two tuples
    - b) Creates a dict
    - c) Raises an error
    - d) Sorts the tuples

**Answers:** 1-c, 2-b, 3-c, 4-c, 5-b, 6-c, 7-b, 8-a, 9-b, 10-a
