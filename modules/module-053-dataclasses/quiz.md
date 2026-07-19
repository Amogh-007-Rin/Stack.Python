# Module 053: Dataclasses — Quiz

1. **Which module provides the `@dataclass` decorator?**
   - a) `data`
   - b) `dataclasses`
   - c) `classes`
   - d) `struct`

2. **What does `@dataclass` automatically generate?**
   - a) `__init__`, `__repr__`, `__eq__`, `__hash__`
   - b) `__init__` only
   - c) `__str__` only
   - d) All magic methods

3. **What does `frozen=True` do?**
   - a) Prevents instantiation
   - b) Makes instances immutable
   - c) Deletes the class
   - d) Freezes the class during import

4. **When should you use `field(default_factory=list)` instead of `field(default=[])`?**
   - a) Always the same
   - b) To avoid mutable default argument issues
   - c) `default` doesn't accept lists
   - d) It's faster

5. **Can dataclasses participate in inheritance?**
   - a) No
   - b) Yes, but only single inheritance
   - c) Yes, fully supported
   - d) Only with `frozen=True`

<details>
<summary>Answers</summary>
1-b, 2-a, 3-b, 4-b, 5-c
</details>
