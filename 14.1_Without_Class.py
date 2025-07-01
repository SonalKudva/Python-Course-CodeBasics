import datetime

# Doing analytics on players without using classes:
def get_average_score(player):
    return sum(player['scores'])/len(player['scores'])

def get_age(player):
    current_year = datetime.datetime.now().year
    return current_year - player['birth_year']

virat = {
    'first_name': 'Virat',
    'last_name': 'Kohli',
    'scores': [],
    'birth_year': 1988
}

virat['scores'].append(80)
virat['scores'].append(100)
virat['scores'].append(0)

david = {
    'first_name': 'David',
    'last_name': 'Waner',
    'scores': [],
    'birth_year': 1986
}

david['scores'].append(35)
david['scores'].append(120)
david['scores'].append(12)

print("Virat")
print(get_average_score(virat))
print(get_age(virat))
print()

print("David")
print(get_average_score(david))
print(get_age(david))