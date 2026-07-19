# Solutions: Data Visualization with matplotlib

## Exercise 1: Line Plot
```python
import matplotlib.pyplot as plt

x: list[int] = [1, 2, 3, 4, 5]
y: list[int] = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Line Plot')
plt.show()
```

## Exercise 2: Bar Chart
```python
import matplotlib.pyplot as plt

products: list[str] = ['A', 'B', 'C', 'D']
sales: list[int] = [120, 90, 150, 80]
colors: list[str] = ['red', 'blue', 'green', 'orange']
plt.bar(products, sales, color=colors)
plt.title('Product Sales')
plt.ylabel('Sales')
plt.show()
```

## Exercise 3: Scatter Plot
```python
import matplotlib.pyplot as plt
import numpy as np

rng: np.random.Generator = np.random.default_rng(42)
x: np.ndarray = rng.random(50) * 100
y: np.ndarray = rng.random(50) * 100
plt.scatter(x, y, marker='^', color='purple', alpha=0.7)
plt.title('Random Scatter Plot')
plt.show()
```

## Exercise 4: Histogram
```python
import matplotlib.pyplot as plt
import numpy as np

rng: np.random.Generator = np.random.default_rng(0)
data: np.ndarray = rng.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
plt.title('Normal Distribution Histogram')
plt.show()
```

## Exercise 5: Pie Chart
```python
import matplotlib.pyplot as plt

labels: list[str] = ['Google', 'Meta', 'Amazon', 'Apple']
values: list[int] = [55, 25, 15, 5]
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Market Share')
plt.show()
```

## Exercise 6: Subplots
```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

x: np.ndarray = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sine')

axes[0, 1].bar(['A', 'B', 'C'], [3, 7, 2])
axes[0, 1].set_title('Bar')

rng: np.random.Generator = np.random.default_rng(0)
axes[1, 0].scatter(rng.random(30), rng.random(30))
axes[1, 0].set_title('Scatter')

axes[1, 1].hist(rng.randn(500), bins=20)
axes[1, 1].set_title('Histogram')

fig.suptitle('2x2 Subplot Grid')
plt.tight_layout()
plt.show()
```

## Exercise 7: Customization
```python
import matplotlib.pyplot as plt
import numpy as np

x: np.ndarray = np.linspace(-10, 10, 100)
y: np.ndarray = x**2
plt.plot(x, y, 'r--', marker='o', markersize=4, label='x²')
plt.grid(True)
plt.xlim(-11, 11)
plt.ylim(-5, 105)
plt.legend()
plt.title('Customized Quadratic Plot')
plt.show()
```

## Exercise 8: Save Figure
```python
import matplotlib.pyplot as plt

x: list[int] = [1, 2, 3]
y: list[int] = [1, 4, 9]
plt.plot(x, y)
plt.title('Saved Plot')
plt.savefig('my_plot.png', dpi=150)

import os
print(f"File exists: {os.path.exists('my_plot.png')}")
```

## Challenge: Multi-series Line Plot
```python
import matplotlib.pyplot as plt
import numpy as np

x: np.ndarray = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), '-', label='sin')
plt.plot(x, np.cos(x), '--', label='cos')
# Tangent: mask values near asymptotes
mask: np.ndarray = np.abs(np.cos(x)) > 0.05
plt.plot(x[mask], np.tan(x[mask]), ':', label='tan', linewidth=1)
plt.ylim(-5, 5)
plt.legend()
plt.title('Trigonometric Functions')
plt.grid(True, alpha=0.3)
plt.show()
```
