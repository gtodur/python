# The Numpy library provides -
#   specialized data structures, 
#   functions, and 
#   other tools 
# for numerical computing in Python.

farming_attributes = [73, 67, 43]
weights = [0.3, 0.2, 0.5]

# dot product = (73 * 0.3) + (67 * 0.2) + (43 * 0.5)
# dot product without numpy
dot_product = 0
for a, w in zip(farming_attributes, weights):
    dot_product += a * w

print(dot_product)

# convert to numpy arrays
# then many functions are available
import numpy as np
farming_attributes = np.array([73, 67, 43])
weights = np.array([0.3, 0.2, 0.5])

print(np.dot(farming_attributes, weights))  # get dot product of 2 arrays
# * performs element wise multiplication between 2 arrays if they are equal
# sum() gives the sum of all elements from the resultant array
print((farming_attributes * weights))       # returns [21.9 13.4 21.5]
print((farming_attributes * weights).sum()) # returns 56.8

# type is ndarray
print(type(farming_attributes))     # returns <class 'numpy.ndarray'>

# can access like arrays
print(farming_attributes[0])    # returns 73

# -------------------------------------------------------------------------------

# Multi-dimensional numpy array

climate_data = np.array([[73, 67, 43],
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]])

print(climate_data)
print(climate_data.shape)   # 2d array (5,3)
print(weights.shape)        # 1d array (3,)

# while reading shape
#   read 1d array as -> no of columns
#   read 2d array as -> no of rows, columns
#   read 3d array as -> no of rows, columns, breadth

# 3D array
array_3d = np.array([[
    [1,2,3], [4,5,6]
],
[
    [7,8,9], [10,11,12]
],
[
    [13,14,15], [16,17,18]
]
])

print(array_3d.shape)   # 3d array (3,2,3)
print(array_3d.dtype)   # returns int64

# we can do matrix multiplication using np.matmul(arr1, arr2) or by using @ operator
print(np.matmul(climate_data, weights))
print(climate_data @ weights)

print("############")
# ----------------------------------------------

climate_data_from_csv = np.genfromtxt(
    './NUMPY/climate.csv', 
    delimiter=',', 
    skip_header=1
)
print(climate_data_from_csv)
print(climate_data_from_csv.shape)

yields = climate_data_from_csv @ weights
print(yields)

# append to csv data fetched
# climate_data_from_csv is the existing data
# we use reshape() on result (yields) to change it from Column,Row format to Row,Column format
# we use axis=1 to denote the dimension of the result to be added
climate_results = np.concatenate(
    (climate_data_from_csv, yields.reshape(9,1)), 
    axis=1
)
print(climate_results)
np.savetxt(
    'climate.csv', 
    climate_results, 
    fmt="%.2f", 
    delimiter=",", 
    header='temperature,rainfall,humidity,yield_apples',
    comments="Added calculated weights to arrive at result")

print(np.genfromtxt(
    'climate.csv', 
    delimiter=',', 
    skip_header=1
))

# NumPy functions for operation on arrays
#    Mathematics:- np.sum, np.exp, np.round, arithmetic operators
#    Array manipulation:- np.reshape, np.stack, np.concatenate, np.split
#    Linear Algebra:- np.matmul, np.dot, np.transpose, np.eigvals
#    Statistics:- np.mean, np.median, np.std, np.max
#    https://numpy.org/doc/stable/reference/routines.html

# ------------------------------------------------------------------------

# NumPy arithmetic operations
#   operations can be done between an array and another array or between an array and a scalar
arr2 = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 1, 2, 3]])

arr3 = np.array([[11, 12, 13, 14], 
                 [15, 16, 17, 18], 
                 [19, 11, 12, 13]])

# Adding a scalar
print(arr2 + 3)
# gives # array([[ 4,  5,  6,  7],
#                [ 8,  9, 10, 11],
#                [12,  4,  5,  6]])

# Element-wise subtraction
print(arr3 - arr2)
# array([[10, 10, 10, 10],
#        [10, 10, 10, 10],
#        [10, 10, 10, 10]])

# Division by scalar
print(arr2 / 2)
# array([[0.5, 1. , 1.5, 2. ],
#        [2.5, 3. , 3.5, 4. ],
#        [4.5, 0.5, 1. , 1.5]])

# Element-wise multiplication
print(arr2 * arr3)
# array([[ 11,  24,  39,  56],
#        [ 75,  96, 119, 144],
#        [171,  11,  24,  39]])

# Modulus with scalar
print(arr2 % 4)
# array([[1, 2, 3, 0],
#        [1, 2, 3, 0],
#        [1, 1, 2, 3]])


# ------------------------------------------------------

# Numpy Array Broadcasting
#   Numpy arrays also support broadcasting
#   It allows arithmetic operations between two arrays with different numbers of dimensions but compatible shapes.

arr2 = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 1, 2, 3]])               
print(arr2.shape)
# (3, 4)

arr4 = np.array([4, 5, 6, 7])
print(arr4.shape)
# (4,)

print(arr2 + arr4)
# array([[ 5,  7,  9, 11],
#        [ 9, 11, 13, 15],
#        [13,  6,  8, 10]])

#   Broadcasting only works if one of the arrays can be replicated to match the other array's shape.

arr5 = np.array([7, 8])
print(arr5.shape)
# (2,)

#print(arr2 + arr5)
# ValueError: operands could not be broadcast together with shapes (3,4) (2,)

# ------------------------------------------------------------------

# Numpy Array Comparison
#   Numpy arrays also support comparison operations like ==, !=, > and so on. 
#   The result is an array of booleans.

arr1 = np.array([
    [1, 2, 3], [3, 4, 5]
])
arr2 = np.array([
    [2, 2, 3], [1, 2, 5]
])

print(arr1 == arr2)
# array([[False,  True,  True],
#        [False, False,  True]])

print(arr1 != arr2)
# array([[ True, False, False],
#        [ True,  True, False]])

print(arr1 >= arr2)
# array([[False,  True,  True],
#        [ True,  True,  True]])

print(arr1 < arr2)
# array([[ True, False, False],
#        [False, False, False]])

print((arr1 == arr2).sum())
# 3


# -----------------------------------------------------------

# Numpy Array Indexing and Slicing
#   Numpy extends Python's list indexing notation using [] to multiple dimensions in an intuitive fashion. 
#   You can provide a comma-separated list of indices or ranges to select a specific element or a subarray (also called a slice) from a Numpy array.

arr3 = np.array([
    [[11, 12, 13, 14], 
     [13, 14, 15, 19]], 

    [[15, 16, 17, 21], 
     [63, 92, 36, 18]], 

    [[98, 32, 81, 23],      
     [17, 18, 19.5, 43]]])

print(arr3.shape)
# (3, 2, 4)

# Single element
print(arr3[1, 1, 2])
# 36.0

# Subarray using ranges
print(arr3[1:, 0:1, :2])
# array([[[15., 16.]],
# 
#        [[98., 32.]]])

# Mixing indices and ranges
print(arr3[1:, 1, 3])
# array([18., 43.])

print(arr3[1:, 1, :3])
# array([[63. , 92. , 36. ],
#        [17. , 18. , 19.5]])

# Using fewer indices
print(arr3[1])

# array([[15., 16., 17., 21.],
#        [63., 92., 36., 18.]])

print(arr3[:2, 1])
# array([[13., 14., 15., 19.],
#        [63., 92., 36., 18.]])

# Using too many indices
#print(arr3[1,3,2,1])
# IndexError: too many indices for array: array is 3-dimensional, but 4 were indexed

# -----------------------------------------------------------

# Other methods to create NumPy arrays

# All zeros
print(np.zeros((3, 2)))
# array([[0., 0.],
#        [0., 0.],
#        [0., 0.]])

# All ones
print(np.ones([2, 2, 3]))
# array([[[1., 1., 1.],
#         [1., 1., 1.]],
#
#        [[1., 1., 1.],
#         [1., 1., 1.]]])

# Identity matrix
print(np.eye(3))    # 1's on diagonals and 0's everywhere else
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])

# Random vector
print(np.random.rand(5))
# array([0.92929562, 0.11301864, 0.64213555, 0.8600434 , 0.53738656])

# Random matrix
print(np.random.randn(2, 3)) # rand vs. randn - what's the difference?
# array([[ 0.09906435, -1.64668094,  0.08073528],
#        [ 0.1437016 ,  0.80715712,  1.27285476]])

# Fixed value
print(np.full([2, 3], 42))
# array([[42, 42, 42],
#        [42, 42, 42]])

# Range with start, end and step
print(np.arange(10, 90, 3))
# array([10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58,
#        61, 64, 67, 70, 73, 76, 79, 82, 85, 88])

# Equally spaced numbers in a range
print(np.linspace(3, 27, 9))
# array([ 3.,  6.,  9., 12., 15., 18., 21., 24., 27.])