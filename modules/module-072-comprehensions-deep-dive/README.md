# Module 072: Comprehensions Deep Dive (List/Dict/Set/Generator)

- **Phase:** 8. Data, Web & APIs
- **Duration:** 1.5 hours

## Learning Objectives

- Write list comprehensions with nested loops and conditionals
- Build dictionaries using dict comprehensions
- Create sets with set comprehensions
- Use generator expressions for memory efficiency
- Apply conditional logic inside comprehensions
- Understand when comprehensions improve readability

## Topics Covered

1. List comprehensions with nested loops
2. Dict comprehensions
3. Set comprehensions
4. Generator expressions (vs. list comprehensions)
5. Conditional logic in comprehensions
6. Nested comprehensions
7. Readability guidelines and best practices

## Prerequisites

Modules 000-070, especially familiarity with loops, lists, dicts, and sets.

## Key Concepts

```python
# List comprehension with condition
evens = [x for x in range(20) if x % 2 == 0]

# Dict comprehension
squares = {x: x**2 for x in range(5)}

# Generator expression
sum_of_squares = sum(x**2 for x in range(1000))
```

## Resources

- Python docs: Data Structures (List Comprehensions)
- PEP 289 – Generator Expressions
- PEP 274 – Dict Comprehensions
