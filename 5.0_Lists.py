items = ["bread", "pasta", "cheese", "veggies"]

# Access the first element
# print("Accessing the first element of the list")
# print(items[0])
# print()

# Access the last element
# print("Accessing the last element of the list")
# print(items[-1])
# print()

# Access list of elements: slice operator
# print("Accessing a list of elements")
# print(items[:2])  # even if do not specify 0, it will still start at the very beginning
# print()

# Add an item to the list
items.append("butter")
print("List that has butter added to it")
print(items)
print()

# Re-arrange the items in the list: want bread and butter next to each other
print("Appending butter right next to bread")
items.remove("butter")
items.insert(1, "butter")
print(items)
print()

# Update any item in the list
print("Update butter to cheese")
items[1] = "cheese"
print(items)
print()
# Note: in prev video we are trying to the above function with strings which are immutable. But, the elements in a list
# can be updated.

# Instead of fruits and veggies, we want almonds
items[3:] = ["almonds"]
print("Instead of fruits and veggies, put almonds")
print(items)
print()

# Use in operator to check if item is within the list
print("Checking if rice in list:", "rice" in items)
print("Checking if bread in list:", "bread" in items)
print()

# Sorting of list
expenses = [30, 1200, 45, 300]

print("Sorting the expenses list in: ")

expenses.sort()
print("Expenses list in ascending order:", expenses)

expenses.sort(reverse=True)
print("Expenses list in descending order", expenses)
print()

# Combine two lists
print("Combining two lists")
food_items = ["bread", "pasta", "fruits"]
bathroom_items = ["shampoo", "soap"]

total_items = food_items + bathroom_items
print("Full list is: ", total_items)
print()

print("All the methods available for list are: ")
print(dir(expenses))
print()

expenses.clear()
print("Clear the expenses list: ", expenses)
print()

# List in Python do not have to be homogeneous: list can contain string, float, boolean, etc.
# Every data type created within the list are called objects which is why we can have a heterogeneous list having
# different data types in the same list.

'''
Takeaways:
1. Lists allow you to store sequential data
2. Lists are ordered, meaning each item has a fixed position unless explicitly changed.
3. Python lists can hold different data types in a single list, including numbers, strings and other lists. This means 
that they are heterogeneous. For example: my_list = ["car", 4.5, True]
4. Lists are mutable, allowing for elements to be added, removed or changed within the same list.
5. List slicing lets you to access a specific range of elements quickly using the syntax. 
list[start:end:step]
'''




