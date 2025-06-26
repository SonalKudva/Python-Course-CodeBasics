# Expenses stored in a list, and we want to find out total expenses:

expenses = [1200, 1300, 1500, 1700]
months = ["January", "February", "March", "April", "May", "June"]

total_expense = expenses[0] + expenses[1] + expenses[2] + expenses[3]
print(f"Total expense via adding individual elements is {total_expense}")
print()

# for loop
print("Printing all values in expenses list")
for expense in expenses:
    print(expense)
print()

total_expenses = 0
for expense in expenses:
    total_expenses += expense

print(f"Total expense via using for loop is {total_expenses}")
print()

# Print the month along with the expenses: like month1 and month 2
# range object allows you to iterate through it
for i in range(len(expenses)):
    print(f"Month {i + 1}, Expense: {expenses[i]}")
print("Total: ", total_expenses)
print()

total = 0
# Shorter way of writing above piece of code
for i, item in enumerate(expenses):  # enumerate is a built-in Python function which will give both element as well
    # as the index
    print(f"Month {i+1}, Expense: {item}")
    total += item

print("Total expenses using enumerate function: ", total)
print()

# Break in for loop
monthly_sales = [42, 38, 33, 38, 40, 45]

threshold = 35

print("Printing the sales amount and month using for loop and zip function")
# Find out when the sales target went below the threshold:
for sales_amount, month in zip(monthly_sales, months):  # tuple(zip()) gives us pairs
    # print(month, sales_amount)
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} is less than threshold in {month}")
        break
    else:
        print(f"Sales amount {sales_amount} is greater than threshold in {month}")
print()

# Benefit of for loop - we can exit the for loop using break statement whenever the objective is met.
# If we want to print the month as well: zip function used as shown above.

'''
If we want to find the first month when we missed the sales amount of the month when we missed the target. If there 
are 1 million values in the list it will keep going on. However, if we put a break statement, the for loop will end as
soon as we find the first sales amount which missed the target.
'''

# USING CONTINUE IN FOR LOOP

print("Printing odd numbers using normal for loop")
# Print only the odd numbers
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
print()

# Using continue in the above for loop
# continue will continue the loop from that point and not execute any code below the continue like
# thus, continue skips the current iteration and proceeds ti the next iteration.

print("Printing odd numbers using continue statement in it")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
print()

# while loop
n = 0
while n < 10:
    print(n)
    n += 1

# Nested for loop:
products = ["iPhone", "iPad", "Macbook"]
regions = ["USA", "China", "India"]
revenue = [20, 23, 45, 18, 17, 12, 12, 9, 5]

i = 0
for product in products:
    for region in regions:
        rev = revenue[i]
        i = i + 1
        print(f"{product} {region}", rev)

# 'else' keyword in for loop: this is to detect when the for loop ends
for i in range(5):
    print(i)
else:
    print("For loop terminated")  # This is executed only when the for loop completed.

# This can be useful in specific condition on a regular basis

'''
Takeaways:
1. For loops iterate over a sequence, such as a list, tuple, or string, executing a block of code for each item.
2. The range() function is often used with for loops to generate a sequence of numbers, facilitating iteration over a
set of steps.
3. Loop control statements like break and continue can alter the flow of a loop, with break exiting the loop and 
continue skipping to the next iteration.
4. enumerate() will allow you to access both the index and the element from a list inside the for loop.
'''