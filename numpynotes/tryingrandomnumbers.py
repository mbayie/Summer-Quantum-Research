import numpy as np

#How to use and generate random numbers

rng = np.random.default_rng(seed=1)

print(rng.integers(low=1, high=7)) #second number is exculsive so it wont be includes
print(rng.integers(1, 7)) #high and low isn't neccessary but can be used for easier readablity

print(rng.integers(low=1, high=7, size = (3))) # creates a 1 x 3 matrix
print(rng.integers(low=1, high=7, size = (3, 2))) # creates 3 X 2 matrix

print(np.random.uniform()) #prints random floating point number between 0-1
print(np.random.uniform(low=-1, high=1, size = 3)) 

#size controls the amount of numbers you get in ur array

np.random.seed(seed = 2) #is you use the same seed u reproduce the same values 


array1 = np.array([1,2,3,4, 5])
print(array1)
rng.shuffle(array1)
print(array1)

rng1 = np.random.default_rng()

fruits = np.array(["apple", "orange", "mango", "grapes"]) #you can neven do this with emojis
fruits = rng1.choice(fruits, size = (3, 2 ))
print(fruits)








