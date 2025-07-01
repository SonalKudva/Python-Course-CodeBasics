'''
Object-Oriented Programming (OOPS):
If we look at any big scale software or enterprise code we will find the usage of OOP. It helps us build bigger
programs in more manageable way.

At the core of OOP is the concept of CLASSES AND OBJECTS.
For example: Human is a class and me and Dhaval are specific instances of human class.
So, when we talk about a class, it is sort of like a blueprint of some category of objects and CLASSES HAVE METHODS AS
WELL AS PROPERTIES.

If we were to define a class for human it would have the following:
Properties: eyes, hands, ears, head, hairs, legs.
Methods/functions (what does human do): eat, drink, sleep, talk, walk, work.

So, human class is a common blueprint for all the humans and a specific human like Dhaval Patel or me, we are the
specific instance or the object of human class.

Another example: car class which would have the following:
Properties: wheels, windshield, engine, etc.
Specific instance of the car class: car we have, i.e., Ciaz is an object of the class car.

Another example:
Let's assume that you are working as a data scientist in some sports analytics company. You want to represent
the player's information and calculate some statistics around it.
'''
import datetime

def get_average_score(player):
    return sum(player['scores'])/len(player['scores'])

def get_age(player):  # this takes player as an argument
    current_year = datetime.datetime.now().year
    return current_year - player['birth_year']

print("Without using classes")
# without using class
# whenever we want to have multiple attributes for some entity, it is better to use dictionary
virat = {
    'first_name': 'Virat',
    'last_name': 'Kohli',
    'scores': [],
    'birth_year': 1988
}
# key = attribute name and value = value of that attribute

virat['scores'].append(80)
virat['scores'].append(100)
virat['scores'].append(0)

print("Average score of Virat:", get_average_score(virat))
print("Age of Virat:", get_age(virat))
print()

# the above things can also be done for david
david = {
    'first_name': 'david',
    'last_name': 'warner',
    'scores': [],
    'birth_year': 1986
}

david['scores'].append(35)
david['scores'].append(120)
david['scores'].append(12)

print("Average score of David:", get_average_score(david))
print("Age of David:", get_age(david))
print()

# using classes
print("Using classes")
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
david.add_score(56)
david.add_score(154)
david.add_score(35)
print("Scores:", david.get_average_score())

'''
We want our class to have certain attributes. Attributes are defined using
__init__() function, which is like a constructor. Constructor is an object
where the object/instance of that class is getting built.
'''

'''
The code with class looks more readable. Object oriented programming, classes and objects will give proper structure to 
the code. It makes it more readable and manageable.
'''

'''
Classes have some in-built methods like
__str__ : this will return a string which will represent that particular
instance of a class. 
'''

'''
Takeaways:
1. OOP makes managing software projects easier.
2. Classes and objects are at the core of OOPS.
3. Classes are like a blueprint of an entity whereas objects represent a specific instance of that class.
For example: Human is a class whereas specific human (say Mira Sharma) is an instance of the class Human.
4. Classes have properties and functions.
5. Use the __init__ method to initialize object properties when an object is created.
6. Methods defined in a class describe the behaviours that objects of that class can perform.
'''