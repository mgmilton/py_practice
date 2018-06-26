import numpy as np


#Create a list and convert it to a numpy array
mylist = [1, 2, 3]
x = np.array(mylist)
x

# Passing a list directly
y = np.array([4,5,6])
y

# Pass in two list for a multidimensional array

m = np.array([[7,8,9],[10,11,12]])
m

# Use the shape method to find the dimmensions of an array (row, columns)
m.shape

# Arrange returns evenly spaced values within a given interval
n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
n

# Reshape returns an array with the same data with a new shape
n = n.reshape(3, 5) # reshape array to be 3x5
n

# linspace returns evenly spaced numbers over a specified interval
o = np.linspace(0,4,9) # returns 0 evenly spaced values from 0 to 4
o

# resize changes the shape and size of array in-place
o.resize(3,3)
o

# ones returns a new array of given shape and type, filled with ones
np.ones((3,2))

# zeros returns a new array of given shape and type, filled with zeros
np.zeros((2,3))

# eye returns a 2-D array with ones on the diagnol and zeros elsewhere
np.eye(3)

# diag extracts a diagonal or constructs a diagonal array.
np.diag(y)

# create an array using repeating list (or see np.tile)
np.array([1,2,3] * 3)

# repeat elements of an array using repeat
np.repeat([1,2,3], 3)


# Combining Arrays
p = np.ones([2,3], int)
p
