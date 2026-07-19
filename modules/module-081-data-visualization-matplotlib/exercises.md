# Exercises: Data Visualization with matplotlib

Assume `import matplotlib.pyplot as plt` for all exercises.

## Exercise 1: Line Plot
Create a line plot of `x = [1, 2, 3, 4, 5]` against `y = [2, 4, 6, 8, 10]`. Add axis labels and a title.

## Exercise 2: Bar Chart
Create a vertical bar chart showing sales: `products = ['A', 'B', 'C', 'D']` with `sales = [120, 90, 150, 80]`. Use different colors for each bar.

## Exercise 3: Scatter Plot
Generate random `x` and `y` data (50 points each) and create a scatter plot with custom markers and colors.

## Exercise 4: Histogram
Generate 1000 random values from a normal distribution using `numpy.random.randn()` and plot a histogram with 30 bins.

## Exercise 5: Pie Chart
Create a pie chart of market share: `['Google', 'Meta', 'Amazon', 'Apple']` with `values = [55, 25, 15, 5]`. Add percentages and a title.

## Exercise 6: Subplots
Create a 2x2 grid of subplots showing a line plot, bar chart, scatter plot, and histogram. Add a main title to the figure.

## Exercise 7: Customization
Plot `y = x**2` for `x` from -10 to 10. Customize: red dashed line, circular markers, grid on, legend, x/ylim.

## Exercise 8: Save Figure
Create any plot of your choice and save it as a PNG file with `dpi=150`. Verify the file exists.

## Challenge: Multi-series Line Plot
Plot three lines (sine, cosine, tangent) on the same axes for `x` from 0 to 2π. Use different line styles, a legend, and a title. Handle the tangent asymptotes gracefully.
