# Read contents of "funny.txt" line by line
f = open("C:\\Users\\DELL\\PycharmProjects\\CodeBasics\\Data\\funny.txt", "r")
# "r" is read mode

print("Contents of 'funny.txt' using open")
for line in f:
    print(line)
print()

f.close()  # This will deallocate the resources that it allocated when it opened the file.


# Sometimes, people forget to close the file. So, Python provides an easy
# code syntax using 'with' statement
print("Contents of 'funny.txt' using with statement")
with open("C:\\Users\\DELL\\PycharmProjects\\CodeBasics\\Data\\funny.txt", "r") as f:
    for line in f:
        print(line)
print()
# we do not have to do f.close because the 'with' will open a context and when you come out pof that
# context when the with block ends, it will close automatically.


# If we want to read all the lines in one single list.
print("Read all the lines in one single list")
with open("C:\\Users\\DELL\\PycharmProjects\\CodeBasics\\Data\\funny.txt", "r") as f:
    lines = f.readlines()
    print(lines)

    # to iterate through the lines
    for line in lines:
        print(line)
print()
# This created a list where every element is a single line.


# To create a file - we will use the "w" (write) mode
with open("Data/love.txt", "w") as l:
    l.write("I love Python\n")
    l.write("I love Meditation\n")

# In order to append the content
with open("Data/love.txt", "a") as l:  # if we make this "w" only the print statements below will be added to .txt file
    l.write("I love Go-lang\n")
    l.write("I love fruits")

# We can laos use .writelines - it takes list as input and every element in hat list is a single line that you want
with open("Data/love.txt", "w") as l:
    l.writelines([
        "I love C++\n",
        "I love scala"
    ])


# Cricket score analysis
player_scores = {}
with open("Data/scores.csv", "r") as s:
    for line in s:
        player, _ , score = line.strip().split(",")  # _ this means ignore that value and .strip will remove extra spac
        score = int(score)

        if player in player_scores:  # if player already exists in player_scores, we append the new score to their list
            player_scores[player].append(score)
        else:  # if the player is not yet in the dictionary, we create a new entry with the score inside the list
            player_scores[player] = [score]

print(player_scores)
print()

# find out min, max and average score for all players
print("Statistics for each player is as follows:")
for player, scores_list in player_scores.items():
    min_score = min(scores_list)
    max_score = max(scores_list)
    avg_score = sum(scores_list) / len(scores_list)
    print(f"{player} ==> Min: {min_score}, Max: {max_score}, Avg: {avg_score}")

# how to remove a file
with open("Data/dummy.txt", "w") as a:
    a.write("whatever")

import os

if os.path.exists("dummy.txt"):  # good practice is to first check if the file exists
    os.remove("dummy.txt")
else:
    print("file does not exist")

'''
Takeaways:
1. The key function for working with files in Python is the open() function. The 
open() function takes two parameters: filename and mode.
2. Here are four different methods (modes) for opening a file:
    "r" - read - default value. Opens a file for reading, error if the file does not exist.
    "a" - append - opens a file for appending, creates the file if it does not exist.
    "w" - write - opens a file for writing, creates the file if it doe not exist.
    "x" = create - creates the specified file, returns an error if the file exists.
3. It is good practice to use the with keyword when dealing with file objects. The advantage
is that the file is properly closed closed after its suite finishes, even if an exception is 
raised at some point
'''