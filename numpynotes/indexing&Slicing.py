import numpy as np

#This file will be about indexing and slicing (grabbing specific parts of an array)


#this is how to index (grab one element)
a = np.array([10, 20, 30, 40, 50])

print(a[0])   # first element → 10
print(a[2])   # third element → 30
print(a[-1])  # last element → 50


#This is slicing (grabbing a range of elements)
print(a[1:4])   # elements at index 1, 2, 3 → [20, 30, 40]
print(a[:3])    # first 3 elements → [10, 20, 30]
print(a[2:])    # everything from index 2 onward → [30, 40, 50]

#indexing a 2D array
b = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

print(b[0, 1])    # row 0, column 1 → 2
print(b[1, :])    # entire second row → [4, 5, 6]
print(b[:, 2])    # entire third column → [3, 6, 9]