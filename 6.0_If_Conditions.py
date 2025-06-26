# Odd even test

n = int(input("Enter a number: "))
# print(n)

# If-else
if n % 2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")
print()

# Above if-else can be done using 'ternary operator', a compact way of writing code
message = "Number is even" if n % 2 == 0 else "Number is odd"
print(message)
print()

# We can use 'negate operator'
if not n % 2 == 0:   # not will just negate, if a statement sis True it will make it False and vice versa
    print(f"Given number {n} is odd")
else:
    print(f"Given number {n} is even")
print()

# Using Python console: we can write quick Python code

# Want to check if number is > 10 and also an even number
if n > 20 and n % 2 == 0:
    print("Yay")
else:
    print("Nay")
print()

indian = ["samosa", "dal", "naan"]
chinese = ["egg roll", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish: ")

if dish in indian:
    print(f"{dish} is Indian")
elif dish in chinese:   # use elif for multiple if conditions
    print(f"{dish} is Chinese")
elif dish in italian:
    print(f"{dish} is Italian")
else:
    print("I do not know which cuisine is this")

'''
Takeaways:
1. 'If' statements execute a block of code only if the condition is True, enabling conditional logic in programs.
2. Use 'elif' to specify additional conditions if the initial 'if' condition fails, allowing for multiple sequential
checks.
3. 'else' provide a fallback block of code when all preceding if and else conditions are false.
4. Combine logical operations like 'and', 'or' and 'not' within if statements to handle complex conditional expressions
5. Nested if statements allow for checking multiple layers of conditions, enabling detailed decision-making process in 
code. 
'''