import numpy as np
import matplotlib.pyplot as plt

# The original function
def f(x):
    return x**2 + 2*x + 1

# The derivative (slope formula)
def df(x):
    return 2*x + 2

# Generate numbers from -5 to 3 for the graph line
x_vals = np.linspace(-5, 3, 100)
y_vals = f(x_vals)

# Create the plot window
plt.figure()
plt.plot(x_vals, y_vals, label="Function Curve", color="blue")

# Pick 3 points and draw a tangent line at each
points = [-3, -1, 1]
for x0 in points:
    y0 = f(x0)
    slope = df(x0)
    
    # Simple line formula: y = mx + c
    # Where c = y0 - (slope * x0)
    c = y0 - (slope * x0)
    
    # Generate a short line segment to show the direction
    x_line = np.linspace(x0 - 1, x0 + 1, 10)
    y_line = slope * x_line + c
    
    # Plot the point and its tangent line
    plt.scatter(x0, y0, color="red")
    plt.plot(x_line, y_line, "--", label=f"Slope at x={x0} is {slope}")

# Add chart decorations
plt.title("Task 1: Slopes and Derivatives")
plt.grid(True)
plt.legend()
plt.show()