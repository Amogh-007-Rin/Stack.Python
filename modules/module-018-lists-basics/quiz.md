# Module 018: Lists: Basics — Quiz

## Question 1
What is the index of the first element in a list?
- A) 1
- B) 0
- C) -1
- D) It depends

## Question 2
Given `fruits = ["apple", "banana", "cherry"]`, what is `fruits[-1]`?
- A) "apple"
- B) "cherry"
- C) "banana"
- D) IndexError

## Question 3
What does `[1, 2, 3] + [4, 5]` produce?
- A) `[5, 7, 3]`
- B) `[1, 2, 3, 4, 5]`
- C) `[1, 2, 3, [4, 5]]`
- D) Error

## Question 4
What is the output of `[0] * 4`?
- A) `[4]`
- B) `[0, 0, 0, 0]`
- C) `0`
- D) `[0, 4]`

## Question 5
What does `nums[2:5]` return from `nums = [0, 10, 20, 30, 40, 50]`?
- A) `[20, 30, 40]`
- B) `[10, 20, 30]`
- C) `[20, 30, 40, 50]`
- D) `[10, 20, 30, 40]`

## Question 6
Are lists mutable?
- A) Yes
- B) No

## Question 7
What does `len([[1, 2], [3, 4], [5, 6]])` return?
- A) 6
- B) 3
- C) 2
- D) 1

## Question 8
What does `print("banana" in ["apple", "cherry"])` output?
- A) True
- B) False
- C) Error
- D) None

## Answers
1. B — Python uses 0-based indexing
2. B — `-1` accesses the last element, "cherry"
3. B — `+` concatenates two lists into one flat list
4. B — `[0] * 4` repeats the list 4 times
5. A — Indices 2, 3, 4 → values 20, 30, 40
6. A — Lists are mutable; you can change elements with assignment
7. B — The outer list has 3 elements, each is a nested list
8. B — `in` checks membership; "banana" is not in the list
