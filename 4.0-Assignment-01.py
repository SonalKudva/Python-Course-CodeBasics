'''
Question 1:
Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.
'''
pi = 22/7
print(f"The data type of pi ({pi}) is: ", type(pi))
print()


'''
Question 2:
Create a variable called 'for' and assign it a value 4. See what happens and find out the reason behind the 
behavior that you see.
'''
# for = 4
# print(for)
# It shows invalid syntax that is because for is one of the 'RESERVED' keywords used for running for loops in Python.
# Thus, we cannot name a variable as 'for'


'''
Question 3:
Below we have defined the variables for storing the principal amount, rate of interest and time. You need to calculate 
the simple interest for 3 years. Once simple interest is calculated, calculate the total amount you will have at the 
end of the tenure.
'''
p = 567.00
r = 5.6
t = 3

simple_interest = p * r * t / 100
print("The amount at end of tenure is:", p + simple_interest, "rupees")
print()


'''
Question 4:
There is a circular pond in a village. This pond has a radius of 84 meter. Can you find the area of the pond?
'''
import math
radius = 84
area = pi * radius**2
print("Area of the pond is:", area, "sq. units")
print()


'''
Question 5:
If there is a 2000 liter water in a square meter, what is the total amount of water in this pond?
'''
water = area * 2000
print("Total amount of water in pond is:", water, "litres")
print()


'''
Question 6:
If you cross a 490-meter-long street in 7 minutes, then what is your speed in meter per seconds. 
Print your answer with only two decimal points.
Hint: Speed = Distance / Time
'''
distance = 490
time = 420
speed = distance / time
print("The speed is:", round(speed, 2), "meters per second.")
print()

'''
Question 7:
Create two variables to store how many fruits and vegetables you eat in a day. The value should be numeric for example:
3 fruits and 4 vegetables. Now Print "I eat x vegetables and y fruits daily" where x and y presents vegetables and 
fruits that you eat every day. Use python f string for this.
'''
fruits = 3
vegetables = 4
print(f"I eat {fruits} fruits and {vegetables} vegetables in a day.")
print()

'''
Question 8:
Create a variable and store the string “The Himalayas are one of the youngest mountain range on the planet.”
1. Print ‘The Himalayas’ using slice operator
1. Print “mountain range” using negative index
1. Print “The Himalayas on the planet” using slice as well as f-string
'''

x = "The Himalayas are one of the youngest mountain range on the planet."
a = x[0:13]
print(a)  # The Himalayans

b = x[-29:-15]
print(b)  # mountain range

c = x[-14:-1]
print(c)  # on the planet

d = print(f"{a} {c}")
print()  # The Himalayans on the planet

'''
Question 9:
You have created a string variable called string=”There are 9 planets in the solar system”. After some time, you have 
realized that your sentence is incorrect and there are only 8 planets, now correct your sentence by replacing the 
incorrect words.
'''
str_1 = "There are 9 planets in the solar system"
print("First statement: ", str_1)

# Mistake I made:
# a = str_1[10:12]
# a = 8
# used slicing and tried to replace, instead I could have used replace function.

# Correct way:
str_1 = str_1.replace("9", "8")

print("Edited statement using replace: ", str_1)

# To modify only a part of string based on index, we can do it as follows:
str_1 = str_1[:10] + "8" + str_1[12:]
print("Edited statement using slicing: ", str_1)
print()

'''
Question 10:
Imagine you are a shop owner tracking sales of three products throughout the day. At the end of the day, you want to 
calculate the total sales from these products. Product quantity and prices are given below in the next code cell,

Task: Write a program that:
1. Calculates the total sales for each product.
1. Summarizes the total sales for the day.
1. Prints this summary in a formatted manner.

Expected Output:
Daily Sales Summary:
- Product 1: Sold 15 units at $20.0 each, Total: $300.0
- Product 2: Sold 10 units at $35.0 each, Total: $350.0
- Product 3: Sold 20 units at $12.0 each, Total: $240.0
Total Sales for the Day: $890.0
'''

# Quantities of each product
prices = [20, 35, 12]
units = [15, 10, 20]

total = 0
final_total = 0
x = 0
for (item, unit) in zip(prices, units):
    x += 1
    total = item * unit
    print(f"Product {x}: Sold {unit} units at ${item} each. Total: ${total}")

    final_total += item * unit

print(f"Total sales for the day is: ${final_total}")