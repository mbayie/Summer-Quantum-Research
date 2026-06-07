import numpy as np
#numpy is all about arrays

#Creating an array
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

#Array attributes
a = np.array([1, 2, 3, 4, 5])

print(a.ndim)    # number of dimensions
print(a.shape)   # size of each dimension
print(a.dtype)   # data type of the elements

#Creating a 2D array -- what Numpy is alledgely good for
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.ndim)
print(b.shape)

#Useful array creation shortcuts
# All zeros
print(np.zeros((3, 4))) #good for initializing arrays B4 filling them with data

# All ones
print(np.ones((2, 3)))

# A range of numbers (like Python's range())
print(np.arange(10)) # like a Python range, but returns an array instead of a list

# A range with a step
print(np.arange(0, 20, 5))  # start, stop, step

# Evenly spaced numbers between two values
print(np.linspace(0, 1, 5))  # 5 numbers between 0 and 1 #good for controlling the space for graphing/math