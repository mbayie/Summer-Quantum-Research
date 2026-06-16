import numpy as np

#pov python is dumb
my_list = [1, 2, 3, 4]
my_list = my_list * 2
print(my_list)

#how to create an array

array =np.array([1,2,3,4])

array = array *2 

print(array)

array = np.array(['A', 'B', 'C']) 
print(array.ndim) #verifies that it is a 1 dimension array

#making a 2 dimesnionsal array
array = np.array([['A','B','C'],
                  ['D','E','F'],
                  ['G','H','I']])
print(array) #prints the array I made
print(array.ndim) #verifies that it is 2D

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']], # top layer
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','&','Z']]]) 

#each list should be consistent wit the number

print(array)
print(array.ndim) # verifies its 3D
print(array.shape) #depth/layers x row x colums

print(array[0][0][0]) #chain indexing in python
print(array[0,0,0]) # multi layer indexing with numpy to get A (faster)

word = array[1, 1, 0] + array[0,0,1] + array[0,0,0] + array[0,2,2] #printing my name
print(word)
