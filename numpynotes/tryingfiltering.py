import numpy as np

#filtering = the process of selecting elements from 
#               an array that match a given condition

#giving ourselves a data set to work with
ages = np.array([[ 21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18,19,20,21]])


#Filtering out for only teenagers
teenagers = ages[ages < 18]

print(teenagers) #boolean indexing changes the shape

print(ages.ndim) #we can see the first one was 2d
print(teenagers.ndim) #while teenagers is 1d

#Filtering for only adults 
adults = ages[ages >= 18 & (ages <65)]

print(adults)

#Filtering for seniors
seniors = ages[ages >= 65]
print(seniors)

#Filtering for even numbers
evens = ages[ages %2 ==0]
print(evens)

#filtering for odd number ages
odds = ages[ages %2 !=0]
print(odds)


#how to keep the shape and dimension of array
adults = np.where(ages >= 18, ages, 0) #0 acts as a fill value fo data that does meet the condition
print(adults)