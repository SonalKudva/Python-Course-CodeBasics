expenses_sergey = [30, 45, 70, 90]
expenses_sundar = [40, 23, 10, 85]

# Anatomy of function:
# Functions allow you to reuse your code.
# A function has a well-defined purpose. This function takes list as an input and iterate over list and add all the
# elements and RETURN the value (it may happen that functions do the necessary computations and not return the value)
def find_total(expenses):  # Function has arguments which is like input. Also not necessay to have arguments.
    '''

    :param expenses: input list containing numbers
    :return: total sum of all numbers in the input list
    '''
    total = 0
    for expense in expenses:
        total += expense

    return total  # Output

total_expenses_sergey = find_total(expenses_sergey)
total_expenses_sundar = find_total(expenses_sundar)

print("Sergey's total expenses using functions: ", total_expenses_sergey)
print("Sundar's total expenses using functions: ", total_expenses_sundar)
print()

# To print the documentation of code (add 3 single quotes in the beginning of the function to get the documentation)
# print(help(find_total)) - this will print the documentation

# #####################################################################################################################

total_expense_sergey = 0
for expense in expenses_sergey:
    total_expense_sergey += expense

print("Total sergey's expense: ", total_expense_sergey)

total_expense_sundar = 0
for expense in expenses_sundar:
    total_expense_sundar += expense

print("Total sergey's expense: ", total_expense_sundar)
print()

# Above, we copied and pasted the code for sundar's expenses. For 5 lists, we would have to repeat this 5 times.
# Functions allow you to reuse your code.

# Exercise 2: Find the volume of a cylinder
def find_cylinder_volume(radius, height=7):  # If we don't supply a height input, default value of height is 67
    print("Radius: ", radius)
    print("Height: ", height)
    volume = 3.14*(radius**2)*height  # volume variable defined inside the function, if try to print volume outside,
    # it won't work. It is accessible only inside the function.
    return volume

r = 10
h = 7

v = find_cylinder_volume(r, h)
print("Normally using the function to print volume:", v)
print()

# Sometimes people may make mistakes and they will exchange the order
print("Calculating volume by exchanging r and h")
v1 = find_cylinder_volume(h, r)
print("Volume by exchanging h and r:", v1)
print()
# To prevent this, we can use keyword arguments

print("Using positional arguments")
v2 = find_cylinder_volume(r, h)  # Positional arguments: order of arguments is confirmed by the position.
print("Volume of cylinder is using positional arguments ", v2)
print()

# Keyword arguments - you specify the keyword in the function
print("Using keyword arguments")
v3 = find_cylinder_volume(radius=r, height=h)
print("Volume of cylinder is using keyword arguments ", v3)  # Here, we can change the order
print()

# Exercise 3: *args
# We want the flexibility where we supply n numbers
# total = sum_all(1, 2, 3, 4, 5) here we wouldn't have that flexibility to do
# So, we use *args and **kwargs

def sum_all(*args):  # *args allows us to give 'n' number of inputs
    total = 0
    # print(args)  # *args converts the input into tuple
    # print()
    for num in args:
        total += num
    return total

total = sum_all(1, 2, 3, 4, 5, 6)


# Exercise 4: **kwargs
# We again want flexibility in the given arguments. For which we will use KEYWORD arguments

def company_info(**kwargs):
    if 'ticker' in kwargs:
        print("Ticker: ", kwargs['ticker'])
    if 'ceo' in kwargs:
        print("Ceo: ", kwargs['ceo'])
    if 'revenue' in kwargs:
        print("Revenue: ", kwargs['revenue'])

# Better way to write above code

    for key in kwargs:  # able to print pe which is not possible in above code
        print(key, kwargs[key])
    print()

company_info(ticker='AAPL', ceo="Tim Cook", revenue='200 billion', pe=20)

# Lambda: quick way/one line way to write functions
def find_square(a):
    return a*a

# Lambda for multiplying two numbers
x = lambda a: a * a
print("Multiplying two numbers using lambda: ", x(5))

# Lambda for adding two numbers
y = lambda a, b: a + b
print("Adding two numbers using lambda: ", y(5, 7))
print()

# All the functions in this code are user defined functions, the functions that we created.

'''
Takeaways:
1. Functions in Python are defined using def keyword, followed by a function name and a parentheses, which may include 
parameters.
2. Parameters allow functions to retrieve inputs, making them flexible and reusable for different data inputs
3. The return statement is used to send a function's result back to the caller, exiting the function and optically 
passing back a value.
4. Default parameters in function definitions provide default values for arguments, simplifying function calls and 
enchanting flexibility.
5. Python supports both positional and keyword arguments, giving more control over how functions are called and how 
arguments are passed to them.
6. Lambda is quick way to define a function in a single line.
'''

