expenses = [1200, 1400, 1700]
# Each of the elements in this list represent same business concept, which is expense.

# But, we will find a requirement in real life where we have elements which represent different concept.
# Example: point in a 2D plane
point = [5, 6]  # [x, y] they represent two different concepts
print("X-axis: ", point[0])
print("Y-axis: ", point[1])
print()

# Better way to use is tuples.

point_2d = (5, 6)

'''
Q. How tuples are different from lists?
A. Tuples are immutable (cannot change elements) and fixed in size (they are memory optimized, store values in an
efficient manner in memory) so access is faster and we can get memory efficient benefits.
Python list is like dynamic array, it can grow/shrink.

Thus, whenever we want to represent a concept where number of items are fixed and we do not want to change them we 
should use tuples. 
'''

def find_pe_and_pb(price, eps, bookvalue):
    pe = price/eps
    pb = price/bookvalue
    return pe, pb  # This returns comma separated values and it will create a tuple out of it and tuple is returned.

pe_ration, pb_ration  = find_pe_and_pb(100, 2, 4)
# In the above case when the tuple is returned, it will have parameters like pe_ration and pb_ratio; it will unpack
# those values into these individual variables.
print("pe_ration and pb_ratio:", pe_ration, pb_ration)
print()
# This is another use of tuples.


# DICTIONARIES

# Let us say we have a programme where we are storing phone numbers.
contacts = [('rachel', 8887771111), ('monica', 9195675555), ('joey', 3332)]  # this is a list of tuples

# One way to store names and phone numbers us by using a list of tuples, with each tuple's first element being name and
# second element being phone number.

# If we want to find out the phone number of Monica
for contact in contacts:
    if contact[0] == "monica":
        print("Monica's contact number is:",contact[1])
print()

# If the above list has a million elements and Monica is all the way towards the end, then we will be iterating through
# all the elements which involves a compute cost (O(n) - n element will have n iterations). Thus, this is not optimized
# in terms of performance.

# Here, we should internally use a DS called 'HASH MAP'.

# There are different ways to implement hashing function. One of the ways is using dictionary in Python.
# Hash maps are implemented using dictionaries in Python
# When we are storing something in a list, the index is an integer index. But, in hash map we can give string as index.
# When we are trying to retrieve value in hash map, it will calculate a hashing function and its performance is constant
# which is O(1)

# Look up by key is O(1) on average
# Insertion/Deletion is O(1) on average

# Dictionary for phonebook
d = {
    'rachel': 8887771111,
    'monica': 9195675555,
    'joey': 3332229999,
}
print("Phone book")
print(type(d))
print()

# People generally use string as keys.

# To access joey's phone number
print(d['joey'])
print()
# Thus internally it is using the hashing function and computing the memory address and it goes to
# memory address and retrieves the value, which is much faster compared to running a for loop.

# When you are unsure of whether a key exists or not we can use the .get function
print(d.get('satya'))  # This will return none
print(d.get('joey'))  # This method (i.e., .get) will not throw an exception or not crash your program.
print()

# To update rachel's phone number
d['rachel'] = 7415296324
print("Phonebook with rachel's updated phone number")
print(d)
print()

# To insert a new record
d['satya'] = 8456329564
print("Phonebook with new entry")
print(d)
print()

# Deleting an element
del d['satya']
print("Deleting the new entry added")
print(d)
print()

# Using in operator
print("Is Abdul present in phone dictionary?", 'abdul' in d)
print("Is Rachel present in phone dictionary?", 'rachel' in d)
print()

# Creating nested dictionary
contact_dict = {
    'rachel': {'phone': 1234, 'address': '1 blue st'},
    'joey': {'phone': 999, 'address': '7 newton blvd'}
}

# To get rachel's phone number
print("Rachel's phone number from a nested dictionary")
print(contact_dict['rachel']['phone'])
print()

print("Rachel's phone number and address from a nested dictionary")
print(contact_dict['rachel'])
print()

# To iterate through an entire dictionary an print all the elements
# name will only give the keys
print("Printing only the names from dictionary d")
for name in d:
    print(name)
print()

# in order to get both the keys and values
print("Printing only the names and phone numbers from dictionary d")
for name, number in d.items():
    print(name, number)
print()

print("Get only the keys (names)")
print(d.keys())

print("Get only the values (phone numbers)")
print(d.values())
print()

# Another nested dictionary
apple_revenues = {
    "USA": {
        "iPhone": 20,
        "iPad": 12,
        "MacBook": 8
    },
    "China": {
        "iPhone": 17,
        "iPad": 9,
        "MacBook": 6
    },
    "India": {
        "iPhone": 9,
        "iPad": 4,
        "MacBook": 2
    }

}

for country, product_data in apple_revenues.items():  # .items() will give key and value
    print(country)
print()

for country, product_data in apple_revenues.items():
    for product, revenue in product_data.items():
        print(f"{country} {product} revenue is: {revenue}")

'''
Takeaways:
1. Tuples are immutable data structures in Python, which means once a tuple is created, its element cannot be changed,
added or removed.
2. Dictionaries in Python are mutable data structures that store key-value pairs, allowing fast data retrieval by key.
3. Dictionary in a Python-specific implementation of HashMap data structure.
4. Keys in dictionaries must be unique and immutable types, such as strings, numbers or tuples, ensuring that each key 
maps distinctly to its value.
5. Both tuples and dictionaries support various methods and operations such as accessing elements, iterating over them 
etc for different efficient data manipulation and retrieval.
'''

# The purpose of .items() function in Python is to iterate through every item of a dictionary
# and get key, value in each iteration.
