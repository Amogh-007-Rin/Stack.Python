# Module 008: Solutions

## Exercise 1
```python
product = "Book"
price = 19.99
print(f"The {product} costs ${price}.")
```

## Exercise 2
```python
print(f"15 * 37 = {15 * 37}")
```

## Exercise 3
```python
pi = 3.1415926535
print(f"{pi:.2f}")      # 3.14
print(f"{pi:.4f}")      # 3.1416
print(f"{pi:.2%}")      # 314.16% (pi * 100 as percent)
```

## Exercise 4
```python
word = "Python"
print(f"|{word:<15}|")
print(f"|{word:>15}|")
print(f"|{word:^15}|")
```

## Exercise 5
```python
score = 85
total = 100
print("Your score is {} out of {}.".format(score, total))
```

## Exercise 6
```python
name = "Bob"
age = 25
print("%s is %d years old." % (name, age))
```

## Exercise 7
```python
print(f"{'Name':<8} {'Age':<5} {'City'}")
print(f"{'Alice':<8} {30:<5} {'London'}")
print(f"{'Bob':<8} {25:<5} {'Paris'}")
```

## Exercise 8
```python
amount = 1234.5678
print(f"${amount:,.2f}")       # $1,234.57
print(f"${amount:>14,.2f}")    # $     1,234.57 (right in 15 chars including $)
```
