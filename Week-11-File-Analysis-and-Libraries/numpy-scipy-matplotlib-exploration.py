# Import libraries

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sp
import pandas as pd
import math

# -----------------------------
# 1. NumPy Functionality
# -----------------------------

print("----- NumPy Operations -----")

arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Square:", np.square(arr))

# -----------------------------
# 2. SciPy Functionality
# -----------------------------

print("\n----- SciPy Operation -----")

# Integration of x^2 from 0 to 3

result = integrate.quad(lambda x: x**2, 0, 3)

print("Integration Result:", result)

# -----------------------------
# 3. Matplotlib Functionality
# -----------------------------

print("\n----- Matplotlib Graph -----")

x = np.arange(1,6)
y = np.square(x)

plt.plot(x, y)

plt.title("Graph of x^2")
plt.xlabel("X values")
plt.ylabel("Square values")

plt.show()


# -----------------------------
# 4. Sympy Functionality
# -----------------------------

print("\n----- Sympy Operations -----")

x = sp.symbols('x')
expr = x**2 + 2*x + 1

print("Expression:", expr)
print("Derivative:", sp.diff(expr))
print("Integral:", sp.integrate(expr))


# -----------------------------
# 5. Pandas Functionality
# -----------------------------

print("\n----- Pandas Operations -----")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [85, 90, 95]
}
df = pd.DataFrame(data)
print(df)
print("Description")
print(df.describe())


# -----------------------------
# 6. Math Functionality
# -----------------------------

print("\n----- Math Operations -----")
print("Square root:", math.sqrt(25))
print("Power:", math.pow(2,5))
print("Factorial of 5:", math.factorial(5))