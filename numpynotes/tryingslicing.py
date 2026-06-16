import numpy as np
array = np.array([[1,2,3,4], 
                  [5,6,7,8],
                [9,10,11,12], 
                [13,14,15,16]])
print(array.ndim)
print(array.shape)

# array [start:end:step]
        #colon acts as slice operator
        #step is the number you are counting by basically
        #(-) reverses the rows

#how to get the first row
print(array[0:0:2])

#selects the first value in every row aka the first colum
print(array[:,0])
         #first number is for row second number is for colum

#prints every colum but the last one
print(array[:,0:3])

#combining row and colum selection
print(array[0:2,0:2]) 
        # selects the first 2 rows of the first 2 lines
        # selects the first 2 colums from the first 2 rows

print(array[0:2, 2:4])


