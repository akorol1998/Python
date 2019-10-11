import numpy as np

# 7
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
arr = np.array([[34,43,73],[82,22,13],[53,94,66]])
print(arr)
arr2 = np.sort(arr, axis=1, kind='quicksort')
# print(arr2)

# The right way
# this is basicaly the way to sort by a specific row, in our case we are sorting by second row
row_sort = arr[:, arr[1,:].argsort()]
print(row_sort)

column_sort = arr[arr[:,1].argsort(), :]
print(column_sort)


# 6 

# arr = np.arange(10,34,1).reshape(8,3)
# np.split() - splits the array either on number of sub_arrays or or at different indents.
# newArray = np.split(arr, 4)
# print(newArray)




#5

# myArray = np.random.rand(3,2)
# print(myArray)
# with np.nditer(myArray, op_flags=['readwrite']) as it:
# 	for x in it:
# 		print(x[...], x, it, '\n')

# arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
# arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])

# third = arrayOne + arrayTwo
# print(third)
# with np.nditer(third, op_flags=['readwrite']) as it:
# 	for x in it:
# 		x[...] = x*2
# print(third)

# 4
# sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
# [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

# Printing all row`s add numbers and columns even numbers
# print(sampleArray[::2,1::2])





# 3
# arr = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]], dtype=np.uint16)

# print(arr)
# Elipsis is an object that can appear in slice notation
# arr2 = arr[..., 1]
# the same as ...
# arr2 = arr[:, 1]
# print(arr2)
# print(arr2.shape)







# 2
# Arange command works similarly to range fucntion
# arr = np.arange(100, 200, 10)

# Reshape command allowas us to reshape the given array to the required shape
# arr = arr.reshape(5,2)


# print(arr)
# print(arr.shape) #Shape
# print(arr.ndim) #NUmber of dimensions
# print(arr.itemsize) #NUmber of dimensions

