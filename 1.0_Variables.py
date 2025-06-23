'''
Variables are containers that stores data.
'''

'''
In Python, everything is an object (every value that a variable is storing is an object).
C++ and Java are strongly typed languages, we have to define the data type of that variable. 
After defining the data type, we cannot store any other value in that variable.
But Python is very flexible, it can store any type of data.
'''

foo = "jalebi"
bar = foo
print(bar)

# Above, it created an object in that it stored the value of jalebi and foo is creating a pointer, pointing to "jalebi"
# When we create the bar variable, we are storing the reference of foo.

# The way to prove the above point is by using "id" function.
# "id" function - prints a unique identifier for an object.

print(id(foo))
print(id(bar))

# id is a unique identifier of an object(different from memory address)
# In the above example, both foo and bar have the same id.
# In memory we have created an object which stores the value 'jalebi' in it and both foo and bar are poinitng to it.

bar = "samosa"
print(id(bar))
print(id(foo))

# Here, the id of bar has changed because it created a separate object in memory and now bar is pointing to that.
# However, the id of foo won't change becuase it is still pointing too our old object which has value jalebi in it.


'''
Takeaways: 
1. Variables are containers that store data in Python program.
2. Variables can store different types of data types such as string, integer, float, boolean
3. Rules of naming variables:
    (a) You cannot use reserve words as variable names (eg. def, True, etc.)
    (b) Variable names must start with a letter or an underscore
    (c) It cannot contain spaces or special characters (@, #, $, %, etc.)
    (d) Underscore is a valid character and can be present at any place in a variable name
'''