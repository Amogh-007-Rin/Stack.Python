# Exercises: Copying Objects

## Exercise 1: Assignment vs Copy
Create `original = [1, 2, 3]`. Assign `ref = original` and `copy = original.copy()`. Modify `ref[0] = 99`. Print all three lists. Which changed?

## Exercise 2: List .copy()
Given `nums = [10, 20, 30]`, create a shallow copy using `.copy()`. Modify the copy's first element. Verify the original is untouched.

## Exercise 3: Dict .copy()
Given `d = {"a": 1, "b": 2}`, create a shallow copy. Modify the copy's `"a"` value. Check that the original is unchanged.

## Exercise 4: Shallow Copy Limitation
Given `nested = [[1, 2], [3, 4]]`, make a shallow copy with `.copy()`. Modify an inner list element via the copy. Does the original change? Why?

## Exercise 5: copy.copy()
Use `import copy` and `copy.copy()` to create a shallow copy of a list. Confirm it behaves the same as `.copy()`.

## Exercise 6: copy.deepcopy()
Use `copy.deepcopy()` on the `nested` list from Exercise 4. Modify an inner element via the deep copy. Verify the original is unchanged.

## Exercise 7: Deep Copy with Mixed Types
Given `data = {"items": [1, 2, {"nested": True}]}`, create a deep copy. Modify the nested dict in the copy. Check the original is unaffected.

## Exercise 8: Copy a Custom Object
Define a simple class `Point` with `x` and `y`. Create an instance and try `copy.copy()` and `copy.deepcopy()`. Do they differ for this case?

## Exercise 9: Performance Consideration
Explain in comments when you would choose shallow copy over deep copy.

## Exercise 10: Preventing Mutation
Write a function `get_avg(nums)` that receives a list and returns the average. Ensure the function does NOT modify the original list (even if it internally sorts).
