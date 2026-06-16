import numpy as np

#Broadcasting allows Numpy to preform operations on arrays with different shapes by vritually expanding dimensions
# array = matrix

#the arrays are compatible if...
#the dimensions have the same size
#OR
#one of the deminsons have a size of one

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)
# output is 
# (1,4)  # looking vertically you can see none of the numbers match up so they are not compatible that way
# (4,1) # However one them is a 1 so it works in that aspect 
#you read from right to left

#Print to see if the broadcasting worked
print(array1 * array2)

#this is basically just like multiplying matrices

#This is where I will make a multiplication table
array3 = np.array([[1,2,3,4,5,6,7,8,9,10]])

array4 = np.array([[1],
                   [2],
                   [3],
                   [4],
                   [5],
                   [6],
                   [7],
                   [8],
                   [9],
                   [10]])
print(array3.shape)
print(array4.shape)

#Making a multiplication table
print(array3 * array4) 
#gives a 10 x 10 Matrix 




