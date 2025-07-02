import datetime

'''
Similar to class CricketPlayer, there is another class below called
TennisPlayer. This has some common methods, similar to CricketPlayer.

We can define the TennisPlayer and CricketPlayer class separately but if
tomorrow we need to define HockeyPlayer and Football player class, there will
be some amount of code duplication.

Inheritance allows you to reuse some of the code.


'''
class TennisPlayer:
    def __init(self, fname, lname, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self. aces = []

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def get_average_aces_per_match(self):
        return sum(self.aces) / len(self.aces)

    def add_aces(self, num_aces):
        self.aces.append(num_aces)

'''
If we want to define hockey/football player class, we would have to do a lot of code duplication. A lot of the methods 
and properties would be the same. 
Inheritance allows us to reuse some of this code. 

'''