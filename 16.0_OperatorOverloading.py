import datetime

class CricketPlayer:   # this is the name of the class
    team_size = 11   # this is common attribute for the class, applicable for all players
    def __init__(self, fname, lname, birth_year, team): # these are variables
        # below this goes all the player specific attributes or properties
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def __str__(self):
        return f"{self.first_name} {self.last_name}, the cricket player from {self.team}"

    # Operator Overloading

    def __lt__(self, other):  # lt - less than, we are overloading the lt operator and giving it a behaviour
        self_avg_score = self.get_average_score()
        other_avg_score = other.get_average_score()
        return self_avg_score < other_avg_score

    def __eq__(self, other):
        self_age = self.get_age()
        other_age = other.get_age()
        return self_age < other_age

# the instance of above class is
virat = CricketPlayer('Virat', 'Kohli', 1988, 'India')
print(virat)  # this means convert virat to str and print it
print("First name:", virat.first_name)
print("Last name:", virat.last_name)
print("Birth year:", virat.birth_year)
print("Age:", virat.get_age())
print("Team:", virat.team)
virat.add_score(37)
virat.add_score(100)
virat.add_score(23)
print("Scores:", virat.get_average_score())
print()

david = CricketPlayer('David', 'Warner', 1985, 'Australia')
print(david)
print("First name:", david.first_name)
print("Last name:", david.last_name)
print("Birth year:", david.birth_year)
print("Age:", david.get_age())
print("Team:", david.team)
david.add_score(37)
david.add_score(23)
david.add_score(85)
print("Scores:", david.get_average_score())
print()

'''
We have these two objects: David and Virat. Wouldn't it be awesome if
if could compare: Is David less than Virat? (David < Virat)?

If we look at our basics, 2 < 3, it is True since they are integer objects.
David < Virat is USER DEFINED. As a user, David < Virat means that if David's
average score is less than Virat's average score, then return True.
'''

# One way to do this is:
print("Is David's average score less than Virat's")
print(david.get_average_score() < virat.get_average_score())  # yes, Virat's average is higher
print()

print("Is David < Virat")
print(david < virat)
print()

print("Is Virat < David?")
print(virat < david)
print()

print("Are David and Virat of the same age?")
print(david == virat)
print()

'''
So, is there a possibility that we can do this where we do not have to
pick specific method

If you have two objects and you have some intrinsic definition of if
one object is less than the other object or not.

print(david < virat) - this threw an error saying that: '<' operator not supported
between instances of the classes

the above issue can be resolved by: OPERATOR OVERLOADING
'<' is an operator which has some defined behaviour for custom classes.
i.e., '<' behaviour is not defined which is why it was giving error. 
But, we have the ability to define that behaviour, by writing a function

Operator overloading has other functions like:
__eq__, __gt__
'''

'''
Takeaways:
1. Operator overloading allows you to define how operations like <, >, ==, +, -, *, etc.
behave for custom objects.
2. Classes and objects are at the core of OOPS.
3. Overloading operators makes your custom classes more intuitive and easier to use.
'''
