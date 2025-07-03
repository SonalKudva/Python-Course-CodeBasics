# FREQUENTLY USED METHOD IN NumPy API
import numpy as np

rev_q1 = np.array([10, 12, 9])
print("Dimension of rev_q1:", rev_q1.ndim)
print()

# Company's 2 quarters' revenue
rev = np.array([[10, 12, 9], [15, 11, 13]])
print("Revenue for 2nd quarter")
print(rev)
print()

print("Dimension of 2 quarters:", rev.ndim)  # 2 dimensional numpy array
# where 1st row is quarter 1 and 2nd row is quarter 2.

# Now we want to locate the revenue of 2nd quarter of 1st month
print("Revenue of 2nd quarter, 1st month:", rev[1, 0])
print()

# Let's say that the revenue for 2nd quarter, 1st month wasn't reported correctly
rev[1, 0] = 14
print("Updated revenue of 2nd quarter")
print(rev)
print()

# Print the datatype by
print("Datatype of rev is:", rev.dtype)  # int64

# Upon creating an array, we can explicitly specify the datatype
rev1 = np.array([[10, 12, 9], [15, 11, 13]], dtype=np.float64)
print("Datatype of rev1 is:", rev1.dtype)
print()

# Now, the number of bytes are going to increase because each of the element is occupying 64 bits/8bytes
# How to print size occupied by each of the element: using .itemsize method
print("Size occupied by each element: ", rev1.itemsize)
print("Number of elements in rev1:", rev1.size)
print()

# Shape method: gives the number of rows and columns
print("Shape of rev1:", rev1.shape)

# Sort the array
print("Sorted rev1 array")
print(np.sort(rev1))  # it is sorting along the last axis, i.e., it is sorting in each of the rows
print()

# If we want to flatten the array
print("Flattened rev1 array")
print(np.sort(rev1, axis=None))   # we can see monthly revenue of a company in ascending order
print()

# Creating an empty np.array with only zeros using np.zeros method
print("A numpy array of zeros")
print(np.zeros((2, 3)))  # this is useful in neural networks because the weights can be easily stored in these 2D array
# or matrices and we can initialize them with zero value.
print()

# Similarly, there is .ones method

# np.arange method:
print("A NumPy array with range 4:", np.arange(5))
print()

# Create an array where elements are between 10 and 20
print("A NumPy array where elements are between 10 and 20:", np.arange(10, 20))

# Create an array where elements are between 20 and 30, with even numbers
# We use: step-size
print("A NumPy array where elements are between 20 and 30 with even numbers:", np.arange(20, 30, 2))
print()

# Method called .linspace() - elements which are linearly spaced.
print("Elements which are linearly spaced:", np.linspace(10, 20, 5))  # last number is: number of elements
print()  # Thus, at equal distance it will create 5 elements

# If we want to flatten and make a single list
print("Make a single list using .ravel():", rev.ravel())
# .ravel method will only create a view and may not modify the original array

# Another way to flatten an array. This will return a new array.
# Thus, there is a subtle difference between the two but from outside their behaviour is almost same.

# Now, instead of 2 rows and 3 columns, we want a different shape
print("Using reshape method to get (3, 2):")
print(rev1.reshape(3, 2))  # Has to be compatible with original shape
print()

print("Using reshape method to get (6, 1):")
print(rev1.reshape(6, 1))
print()

# If we want to find minimum and maximum revenue
print("Minimum revenue in rev1:", rev1.min())
print("Maximum revenue in rev1:", rev1.max())
print()

# NOTE: NumPy is implemented in C, therefore it is very fast.

# If we want the sum of all the revenues
print("Sum of all the revenues in Q1", rev1.sum(axis=1))  # it will add along the rows
print("Sum of revenues of respective months in each quarter:", rev1.sum(axis=0))  # it will add along the columns

'''
Question: What is axis parameter?
Answer: Axis parameter is used to specify the direction in which an operation 
should be performed. It helps determine whether to operate row-wise or column-wise
in a multi-dimensional array or DataFrame.
axis = 0, operates along the columns (downwards)
axis = 1, operates along the rows (horizontally)
'''


'''
Takeaways:
1. You do not have to remember API syntax. In real life, people always refer to NumPy documentation, ChatGPT or Google 
to know the syntax
2. sum(), min(), max(), std(), are used for doing quick statistical analysis
3. Given below are functions used for:
ndim: to find out array's dimension
itemsize: element byte size
size: total number of elements
shape: size of each dimension
'''