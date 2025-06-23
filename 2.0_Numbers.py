import math

base = 10
height = 7

area = (base * height)/2

x = 10
y = 3

# Addition
print("Addition: ", x + y)

# Subtraction
print("Subtraction: ", x - y)

# Division
print("Division: ", x/y)

# If we just want the integer part
print("Only integer part: ", x//y)

# If we want the remainder
print("Remainder: ", x%y)

# Exponent
print("Exponent: ", x**y)
print()

# There is an order in which operations are performed
print("Value of 10+2*3 is: ", 10+2*3)
print("Value of (10+2)*3 is: ", (10+2)*3)
print()

# Using scientific notation
f = 2.3e4  # 23,000
g = 1e4  # 10,000
# e raised to four means after 1 you have 4 zeros
# e^4 is 10^4 (after 1 there are 4 zeros)
h = 2.3e-3  # 0.0023
i = 1e-3  # 0.001

print("Using scientific notation 1e4: ", g)
print("Using scientific notation 2.3e4: ", f)
print("Using scientific notation 1e-3 :", i)
print("Using scientific notation 2.3e-3: ", h)
print()

# In order to know what all functions a module has
print("All functions in math module: ")
print(dir(math))
print()

print("Binary representation of 5: ", format(5, 'b'))
# RAM in computer: single unit to store value is bit (which is 1 or 0)
# 8 bits = 1 byte


'''
Takeways:
1. Integer number store whole numbers (without decimal part) eg. 57
2. Float numbers store fractional numbers with whole and decimal part, eg. 57.23
3. type(variable_name) can be used to detect the data type of a variable
4. '/' operator is used for division
5. '//' operator is used to retrieve the integer part of the division
6. '%' is a modulo operator, it returns the remainder of a division operator.
7. x**y will return x raised to the power y
8. You can do type casting using functions such as float(), int(), str(), etc.
9. float("10.2") will convert string value "10.2" to a float value 10.2.
10. math is a handy module in Python that allows you to run different functions such as sqrt, float, ceil, etc.
'''