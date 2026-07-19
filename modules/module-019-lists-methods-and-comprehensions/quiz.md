# Module 019: Lists: Methods & Comprehensions — Quiz

## Question 1
What does `a.append([4, 5])` do to list `a = [1, 2, 3]`?
- A) Adds 4 then 5 as separate elements
- B) Adds `[4, 5]` as a single element → `[1, 2, 3, [4, 5]]`
- C) Raises an error
- D) Replaces the last element with `[4, 5]`

## Question 2
What's the difference between `remove(x)` and `pop(x)`?
- A) `remove` deletes by index, `pop` deletes by value
- B) `remove` deletes by value, `pop` deletes by index and returns it
- C) They are the same
- D) `pop` returns nothing, `remove` returns the value

## Question 3
What is the result of `[x ** 2 for x in range(5)]`?
- A) `[1, 4, 9, 16, 25]`
- B) `[0, 1, 4, 9, 16]`
- C) `[0, 2, 4, 6, 8]`
- D) `[1, 2, 3, 4, 5]`

## Question 4
After `nums = [3, 1, 2]; nums.sort()`, what is `nums`?
- A) `[3, 1, 2]`
- B) `[1, 2, 3]`
- C) `None`
- D) `[2, 1, 3]`

## Question 5
What does `sorted(list)` do compared to `list.sort()`?
- A) Both modify in place
- B) `sorted()` returns a new list, `sort()` modifies in place
- C) `sorted()` modifies in place, `sort()` returns a new list
- D) Both return a new list

## Question 6
What does `["even" if n % 2 == 0 else "odd" for n in [1, 2, 3]]` produce?
- A) `["even", "even", "even"]`
- B) `["odd", "odd", "odd"]`
- C) `["odd", "even", "odd"]`
- D) `[True, False, True]`

## Question 7
What happens if you call `remove()` with a value not in the list?
- A) Nothing happens
- B) Returns `None`
- C) Raises `ValueError`
- D) Removes the last element

## Answers
1. B — `append` adds its argument as a single element
2. B — `remove(x)` removes first occurrence of value `x`; `pop(x)` removes element at index `x` and returns it
3. B — `range(5)` is 0, 1, 2, 3, 4; squares: 0, 1, 4, 9, 16
4. B — `sort()` sorts the list in place (ascending by default)
5. B — `sorted()` returns a new sorted list; `sort()` modifies in place and returns `None`
6. C — 1 → "odd", 2 → "even", 3 → "odd"
7. C — `remove()` raises `ValueError` if the value is not found
