'''
Some basic exceptions using the Python console.
If we divide a number by 0, it gives ZeroDvisionError. This error is
Python's built-in exception

(Google Python's built-in exceptions)
'''

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

# print("Divide x/y is: ", d)  # This throws and exception and code below this line
# won't be executed.

# in real life situations it is better to execute code below that line. This
# process is called exception handling. In context of programming, we would handle that
# exception and continue the code execution and reach to your goal.

# To handle exceptions, we use TRY-EXCEPT block.

d = 0
try:
    d = x / y
except:  # This is only executed when exception occurs
    print("Exception is handled")

print("Division is: ", d)
print()

# It is a good practice to use specific exception as follows:
try:
    d = x / y
    a = "baby yoda" + 56
except ZeroDivisionError as ze:
    print("Exception occurred:", ze)
    d = -1
except TypeError as te:
    print("Exception occurred:", te)
    d = -1
except Exception as e:  # This is a generic class, it is like the father of all the exceptions.
    # It can catch all exceptions. But its usage is not encouraged since we want to have some predictability. Better to
    # to use specific exceptions
    print("Generic exception:", e)
    d = -1

print("Division is: ", d)
print()

# Use of finally: that piece of code will get executed no matter what
try:
    file = open("C:\\Users\\DELL\\PycharmProjects\\CodeBasics\\Data\\customers.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File was not found")
finally:  # This piece of code will be executed no matter what
    file.close()
    print("File closed.")

# How to throw an exception. Many times, it is beneficial if you throw an exception
def deposit(amount):
    global balance
    if amount <= 0:
        raise ValueError("Amount must be positive")
    balance += amount

# Creating a custom exception class
class InsufficientFunds(Exception):
    pass

balance = 0
def withdraw(amount):
    global balance
    if amount > balance:  # Here we are creating a custom exception class
        raise InsufficientFunds(f"Not enough funds. Current balance: {balance}")
    balance -= amount

deposit(100)
deposit(17)
withdraw(5)
print(balance)

"""
Takeaways:
1. Exception handling ensures that programs can address and recover from errors during execution without crashing.
2. Using try and except blocks allows developers to separate normal code from error handling code, enhancing readability.
3. Specifying particular exceptions to catch enables targeted responses to different error types, improving error 
resolution effectiveness.
4. The finally block executes code regardless of whether an exception was raised or not, ensuring that cleanup and 
release of resources can always occur.
"""