# Module 056: Error Handling — Solutions

```python
# 1. Basic try/except
def safe_divide(a: float, b: float) -> float | str:
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"


print(safe_divide(10, 2))
print(safe_divide(10, 0))

# 2. Multiple except
def parse_int(value: object) -> int | str:
    try:
        return int(value)  # type: ignore
    except ValueError:
        return "Error: cannot convert to int"
    except TypeError:
        return "Error: wrong type"


print(parse_int("42"))
print(parse_int("abc"))
print(parse_int(None))

# 3. try/except/else/finally
def read_file_safe(path: str) -> str | None:
    try:
        f = open(path, "r")
    except FileNotFoundError:
        return f"File {path} not found"
    else:
        content = f.read()
        f.close()
        print(f"Successfully read {path}")
        return content
    finally:
        print("Operation attempted")


print(read_file_safe("nonexistent.txt"))

# 4. raise
def withdraw(balance: float, amount: float) -> float:
    if amount < 0:
        raise ValueError("Withdrawal amount cannot be negative")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


try:
    withdraw(100, -5)
except ValueError as e:
    print(f"Error: {e}")

try:
    withdraw(100, 200)
except ValueError as e:
    print(f"Error: {e}")

# 5. Multiple exception types
def process_data(data: dict) -> str:
    try:
        value = data["key"]
        result = 100 / value  # type: ignore
        return f"Result: {result}"
    except TypeError:
        return "TypeError: invalid operation"
    except ValueError:
        return "ValueError: bad value"
    except KeyError:
        return "KeyError: missing key"


print(process_data({"key": 10}))
print(process_data({"wrong": 10}))
print(process_data({"key": "abc"}))
```
