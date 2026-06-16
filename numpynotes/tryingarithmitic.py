import numpy as np

#Scalar arithmetic

array = np.array([1,2,3])

#Basic operations
print(array +1) # adds 1 to each element
print(array -1) #minus 1 from each
print(array * 3) #multiplies each by 3
print(array /3) # divides each one by 3
print(array **5) # raises each one to the fifth power

#Vectorized math funcs

array = np.array([1,2,3])
print(np.sqrt(array))

array = np.array([1.7, 2.43, 3.67])
print(np.round(array)) #round to nearest whole
print(np.floor(array)) #always rounds down
print(np.ceil(array)) # always rounds up
print(np.pi) #3.14

#practicing by doing the area of a circle
radii = np.array([1,2,3])
print(np.pi * radii ** 2)


#Element wise arithmetic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

#comparision operators

scores = np.array([91, 55, 100, 67, 82, 28])

print(scores == 100) #boolean operator
print(scores >=60) #see who passed the test
print(scores <=60) #see who failed

scores[scores <60] = 0
print(scores) # giving people who failed a zero :(


