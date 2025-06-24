# Below variables contain string data
first = "Mohan"
last = "Sharma"

# To specify string data, we use either " " or

# To print fullname
name = first + " " + last
# print("Full name: ", name)
print()
new_name = "Mohan Sharma"

# Other way to create string: Python format string
name = print(f"Name is: {first} {last}")
print()

# Format/f strings are useful when we have too many variables in creating the
# final text.

# For example, we want to print "Mohan Sharma's age is 28"
age = 28

print(f"{first} {last}'s age is {age}.")
print()

# To obtain first character of the string
print("First character of string Mohan Sharma is:", new_name[0])
print()

# Print the first name
print("First name is:", first[0:5])  # need to give additional index since last is not inclusive
print()

# Print the last name
print("Last name is:", last[0:6])
print()

# Other way of printing the last name
print("Another way to print last name is:", new_name[6:])  # no need to specify last stop value, takes entire string
print()

# Reverse operator
# print(last[::-1])

# Use len function to get the size of the string
print("Length of the string is:", len(new_name))

# If we want to change 'Mohan' to 'Sohan'
# new_name[0] = 'S'
# print(new_name) # String objects are immutable, upon initializing them they cannot be changed.

# If inside the string we have single quotes, then the string must be put inside double quotes and vice versa
# If inside the string we have double quotes, then the string must be put inside single quotes.

# \n - new line character. To format strings properly, use the print statement.

recipe = ("Veg biryani with saffron, cardamom and cloves garnished with fried onions and cilantro")
print(recipe)
print()

# To check if cardamom is present in the recipe
spice = "cardamom"
print("Is cardamom present in recipe: ", spice in recipe)
print()

# To check at what index cardamom is present
print("Index of cardamom: ", recipe.find(spice))
print()

# To check if milk is used in the recipe
ingredients = "milk"
print("Is milk present in the recipe: ", ingredients in recipe)
print()


# SOME USEFUL FUNCTIONS IN THE STRING
s = "Patient was charged 100$ for the lab test"

# To check all the available functions
# print("To check all the functions available for string")
# print(dir(s))
# print()

# 1. replace function
s = s.replace("100$", "10$")
print("Updated charge: ", s)
print()

#  2. upper function - converts all the characters to upper case
s = s.upper()
print("Upper case string: ", s)
print()

# 3. lower function - converts all characters to lower case
a = "ABC"
print("Lower case string: ", a)
print()

# 4. isdigit: check if something only contains digit
b = "510"  # Numbers also need to be in quotes for '.isdigit' function
c = "F1-603"

print("Does '510' it only contain digits: ", b.isdigit())
print()

print("Does 'F1-603' only contain digits: ", c.isdigit())
print()

# 5. Another way to find index for 10$
print("Index for  10$: ", s.index("10$"))
print()

# 6. Join string and dollar
text = "My age is: "
age = 38
# print(text + age)  # This gives an error as can only concatenate str and not int

# Solution
print(text + str(age))
# It cannot join string with number. So, we had to convert int to str and then join them
print()

# 7. split function
tickers = "AAPL|NVDA|RIL|GOGL"
print("Split characters: ", tickers.split("|"))
print()

print("Split only 2 words: ", tickers.split("|", maxsplit=2))
print()

# 8. Extra white space removal
data = " hey, we have to go there, you coming there ? "
print("Data with white space removed: ", data.strip())
print()

# 9. Figure out the file type
file_name = "report.pdf"
print("The file type is .pdf: ", file_name.endswith(".pdf"))
# Similarly, there is a function called starts with

'''
Takeaways:
1. In Python, strings are immutable, meaning they cannot be changed once created.
2. Access specific characters or substrings in Python using indexing (eg., name[0] and slicing (eg., name[1:5])
3. Use string formatting techniques like f-strings (e.g., f{variable} for easier and more readable string composition 
in Python
4. Python provides built-in methods for string such as [.upper(), .lower(), .split(), and .strip()]
'''



