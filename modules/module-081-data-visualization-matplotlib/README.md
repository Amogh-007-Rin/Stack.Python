# Module 081: Data Visualization with matplotlib

- **Phase:** 9. Databases & Web Apps
- **Duration:** 2.5 hours

## Learning Objectives

- Create line plots, bar charts, scatter plots, histograms, and pie charts with matplotlib
- Customize figures with labels, titles, legends, colors, styles, and markers
- Use subplots to display multiple charts
- Save figures to files

## Topics Covered

1. matplotlib.pyplot basics: figure and axes
2. Line plots with plt.plot
3. Bar charts with plt.bar and plt.barh
4. Scatter plots with plt.scatter
5. Histograms with plt.hist
6. Pie charts with plt.pie
7. Labels, titles, legends
8. Saving figures with plt.savefig
9. Subplots with plt.subplots
10. Customization: colors, styles, markers

## Prerequisites

Modules 000-080.

## Key Concepts

```python
import matplotlib.pyplot as plt

# Line plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Line Plot')
plt.show()

# Subplots
fig, axes = plt.subplots(2, 2)
axes[0, 0].bar(['A', 'B', 'C'], [3, 7, 2])
axes[0, 1].scatter([1, 2, 3], [4, 5, 6])
plt.savefig('output.png')
```

## Resources

- matplotlib documentation: https://matplotlib.org
- pyplot tutorial
- matplotlib gallery for inspiration
