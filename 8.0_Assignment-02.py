'''
Question 1:
You are a Marvel fan and created a list of superheroes.
avengers  = [‘Iron Man’, ‘Captain America’, ‘Black Widow’, ‘Hulk’, ‘Thor’, ‘Hawkeye’]
Using this list, calculate how many members in the Avengers team?
'''
avengers = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]

# Number of members in Avengers team:
print("Total members in Avengers: ", len(avengers))
print()

'''
Question 2:
Awesome. Now Iron Man made Spider-Man a new member of the Avengers, add him to your list at the end
'''
avengers.append("Spider Man")
print("Avengers with new added member")
print(avengers)
print()

'''
Question 3:
Looks like you are loving this avengers exercise already. Let's add a twist to it. Everyone came to a conclusion that 
Captain America is the leader of the Avengers, so please add him before the Iron Man. Hint: You can first remove him 
from the list and add before the Iron Man. To remove him you can use a method called .pop()
'''
iron_man = avengers.pop(0)
captain_america = avengers.pop(0)
avengers.insert(0, captain_america)
avengers.insert(1, iron_man)
print("The repositioned list is")
print(avengers)
print()

'''
Question 4:
Thor and Hulk are getting angry easily and fight with each other. So you have to separate them with each other. 
To separate them, move “Black Widow” in between them.
'''
print("List after separating Hulk and Thor")
hulk = avengers.pop(3)
avengers.insert(2, hulk)
print(avengers)
print()

'''
Question 5:
Below list contains scores of students in a class as per their roll number. Which means the first element is for roll 
# 1, second one is for roll # 2 and so on. Print the scores of,
1. The first student
1. The last student
1. First 3 students
1. Scores of roll # 3, 4 and 5
'''
scores = [92, 85, 76, 58, 89, 91, 73, 84]

# Score of first student
print("The score of roll number 1 is:", scores[0])

# Score of last student
print("The score of last student is:", scores[-1])

# Score of first three students
print("The scores of first three students:", scores[0:3])

# Score of roll numbers 3, 4, and 5
print("The score of roll numbers 3, 4 & 5 is:", scores[2:5])
print()

'''
Question 6:
We got a result of one more student which is 83 marks. Append this to the scores at the end and print the list
'''
scores.append(83)
print("New scores list is")
print(scores)
print()

'''
Question7:
Categorizes each score into a grade based on the following thresholds:
1. A: 90 to 100
1. B: 80 to 89
1. C: 70 to 79
1. D: 60 to 69
1. F: Below 60
Count the number of students in each grade category and print the summary of how many students received each grade. 
Expected output
Grade Summary:
- A: 2 students
- B: 4 students
- C: 2 students
- D: 0 students
- F: 1 students
'''
# if grade >= 90 and grade <= 100:
#     print("A")
# elif grade >= 80 and grade <= 89:
#     print("B")
# elif grade >= 70 and grade <= 79:
#     print("C")
# elif grade >= 60 and grade <= 69:
#     print("D")
# else:
#     print("F")

grade_A = grade_B = grade_C = grade_D = grade_F = 0
for score in scores:
    if score >= 90:
        grade_A += 1
    elif score >= 80:
        grade_B += 1
    elif score >= 70:
        grade_C += 1
    elif score >= 60:
        grade_D += 1
    else:
        grade_F += 1

print(f"A: {grade_A} students")
print(f"B: {grade_B} students")
print(f"C: {grade_C} students")
print(f"D: {grade_D} students")
print(f"F: {grade_F} students")
print()

'''
Question 8:
Managing inventory efficiently is crucial for businesses to ensure they do not run out of key products. This exercise 
simulates a simple inventory management system where the user can see which items are below the minimum stock level and
need reordering. Below you have two lists that stores product names and their inventory stock levels. Using that,

1. Check each item to see if its stock level is below a minimum threshold.
1. If the stock level is below the minimum, add the product's name to a reorder list.
1. Print a list of products that need to be reordered.

Expected Output:
Items to Reorder:
- Pears
- Grapes
'''

# Lists to store product names and stock levels
product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]

# after practicing
min_thres = 10
reorder = []
for product, stock in zip(product_names, stock_levels):
    if stock < min_thres:
        reorder.append(product)

print("Items to reorder: ", reorder)

print("To print according to solution")
print("Items to Reorder:")
for i in reorder:
    print(f"- {i}")
print()

# Previously done
print("Previously done")
minimum_stock = 10  # Minimum stock before reordering

reordering_list = []

for fruit, level in zip(product_names, stock_levels):
    if level < minimum_stock:
        reordering_list.append(fruit)

print("Items to reorder: ")
print(reordering_list)
print()

# Solution:
# Loop through the indices of the lists
reorder_list = []
for i in range(len(product_names)):
    if stock_levels[i] < minimum_stock:  # Check if stock is below minimum
        reorder_list.append(product_names[i])  # Append product name to reorder list

# Print out the reorder list
print("Items to Reorder:")
for product in (reorder_list):
    print(f"- {product}")