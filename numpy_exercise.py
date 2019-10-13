import numpy as np

#10 Create a two 2-D array and Plot it using matplotlib
arr = np.array([[14,54,67], [3,4,5]])
arr2 = np.array([[298,1,23]])

arr3 = np.vstack((arr, arr2))
print(arr3)





# 9 Following is the input NumPy array delete column two and insert following new column in its place.

# arr = np.array([[34,43,73],[82,22,12],[53,94,66]])
# new_col = np.array([[10,10,10]])
# print(arr)
# arr = np.delete(arr, 1, axis=1)
# arr = np.insert(arr, 1, new_col, axis=1)
# print(arr)



# 8 Following is the 2-D array. Print max from axis 0 and min from axis 1

# arr = np.array([[34,43,73],[82,22,12],[53,94,66]])

# mina = np.amin(arr, 1)
# print(mina)

# maxa = np.amax(arr, 0)
# print(maxa)
# print(np.mean(arr,1))

# arr = np.array([[34,43,73],[82,22,12],[53,94,66]])
# print(arr)
# row_sort = arr[:, arr[1, :].argsort()]
# col_sort = arr[arr[:, 1].argsort(), :]

# print('\n', row_sort, "\b")
# print(col_sort,)


# 7 Sort following NumPy array
# # sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
# arr = np.array([[34,43,73],[82,22,13],[53,94,66]])
# print(arr)
# arr2 = np.sort(arr, axis=1, kind='quicksort')
# # print(arr2)

# # The right way
# # this is basicaly the way to sort by a specific row, in our case we are sorting by second row
# row_sort = arr[:, arr[1,:].argsort()]
# print(row_sort)

# column_sort = arr[arr[:,1].argsort(), :]
# print(column_sort)


# 6 Split the array into four equal-sized sub-arrays

# arr = np.arange(10,34,1).reshape(8,3)
# np.split() - splits the array either on number of sub_arrays or or at different indents.
# newArray = np.split(arr, 4)
# print(newArray)




#5 Add the following two NumPy arrays and Modify a result array by calculating the square root of each element

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

# 4 Following is the given numpy array return array of odd rows and even columns
# sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
# [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

# Printing all row`s odd numbers and columns even numbers
# print(sampleArray[::2,1::2])





# 3 Following is the provided numPy array. return array of items in the third column from all rows

# arr = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]], dtype=np.uint16)
# print(arr)
# Elipsis is an object that can appear in slice notation
# arr2 = arr[..., 1]
# the same as ...
# arr2 = arr[:, 1]
# print(arr2)
# print(arr2.shape)







# 2 Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10

# Arange command works similarly to range fucntion
# arr = np.arange(100, 200, 10)


# Create a 4X2 integer array and Prints its attributes
# Reshape command allowas us to reshape the given array to the required shape
# arr = arr.reshape(5,2)

# print(arr)
# print(arr.shape) #Shape
# print(arr.ndim) #NUmber of dimensions
# print(arr.itemsize) #NUmber of dimensions

