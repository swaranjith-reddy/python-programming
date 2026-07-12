import numpy as np

# Create 1D array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Check datatype
print("Data type:", arr.dtype)

# Shape of array
print("Shape:", arr.shape)

# Number of dimensions
print("Dimensions:", arr.ndim)

# Mathematical operations
print("Array + 5:", arr + 5)
print("Array * 2:", arr * 2)

# Create 2D array
arr2 = np.array([[1,2,3],[4,5,6]])
print("\n2D Array:\n", arr2)

# Sum of elements
print("Sum of elements:", np.sum(arr))

# Mean value
print("Mean:", np.mean(arr))

# Maximum value
print("Maximum:", np.max(arr))
