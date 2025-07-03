import numpy as np
import sys
import time

# NumPy = Numeric Python

arr = np.array([1, 2, 3])

# BENEFITS OF NUMPY OVER PYTHON LISTS
# 1. np.array occupies less memory in comparison to Python lists.
python_list = list(range(100))
numpy_array = np.arange(100)

# Note: Size and byte memory are two different things. Each of the element, which is an integer will occupy couple of
# bytes.

# So, let's look at how much memory Python list is occupying is RAM
print("Size of Python list in bytes:", sys.getsizeof(python_list[0])*len(python_list))
print("Size of NumPy array in bytes:", numpy_array.nbytes)
# So, the memory occupied by Python list is almost 6 times that of NumPy array.
print()

'''
Question: Why Python list occupies so much memory?
Answer: Python supports non-homogeneous elements. If we have a Python list - one element can be string, other can be
float and so on. In order to support that, it has to store extra metadata. Also, another thing to note that these
addresses in the memory might be scattered.
Thus, due to metadata and fragmented storage, when we are accessing all those elements, it will be a little slow.
'''

# 2. NumPy array stores data in contiguous location of memory. Because of this, the total memory occupied by NumPy array
# is less and accessing becomes faster.

size = 1000000  # size = 1 Million
l1 = list(range(size))
l2 = list(range(size))
# What we want to do with the above two lists are: take first element from l1
# and add to 1st element of l2, and so on. So, each of the index, add those elements
# and create a new list l3.
# In Python lists, this is not possible. So, we will have to use a list comprehension.

start_time = time.time()
l3 = [x + y for x, y in zip(l1, l2)]
end_time = time.time()
# print("l3 list:", l3)
print("Python list took:", end_time - start_time)
print()

n1 = np.arange(size)
n2 = np.arange(size)
n3 = n1 + n2

# 3. Convenient use with built-in functions
l1 = list(range(5))
l2 = list(range(5))
print("Adding list l1 and l2:", l1 + l2)  # Since we are adding Python list. it does concat and not add respective vals
print()

# Thus, in order to get the addition of the elements in the list we need to use LIST COMPREHENSION
l3 = [x + y for x,y in zip(l1, l2)]
print("Adding l1 and l2 using list comprehension:", l3)
print()

# Question: What is zip?
a1 = [1, 2, 3]
a2 = [8, 7, 9]

for i, j in zip(a1, a2):
    print(i, j)
print()

print(tuple(zip(a1, a2)))

'''
To summarize, we looked at 3 benefits:
1. NumPy occupies less memory.
2. It is much faster.
3. It has alot of convenient uses with built-in functions.
'''

'''
Takeaways:
1. NumPy (Numeric Python) is a popular library used for data analysis, ML and scientific computing.
2. Any person doing data analysis or ML in Python, uses NumPy almost on a daily basis.
3. NumPy arrays offers several benefits over plain Python list such as:
    - Less memory consumption.
    - Fast operations.
    - Convenient APLIs for variety of mathematical functions.

'''