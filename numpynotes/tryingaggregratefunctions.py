import numpy as np
#aggregate functions = summarize data and typically return a single value

#making data to work with
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])



print(np.sum(array)) #print the sum of all the numbers in the matrix
print(np.mean(array)) #print the mean of data
print(np.std(array)) #standard deviation 
print(np.var(array)) #sq of std
print(np.min(array)) #smallest value
print(np.max(array)) #highest value
print(np.argmin(array)) #arg function tells you the position of where the min value is
print(np.argmax(array))

#sum all colums
print(np.sum(array, axis=0))

#sum all rows
print(np.sum(array, axis=1)) 

