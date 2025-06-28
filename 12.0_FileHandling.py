# Read file ine by line
f = open('C:\\Users\\DELL\\PycharmProjects\\CodeBasics\\Data\\funny.txt', "r")

for line in f:
    print(line)

f.close()

# if we do not want to do f.close():
with open('C:\\Users\\DELL\\PycharmProjects\\CodeBasics\\Data\\funny.txt', "r") as f:
    # This with will open a context, after coming out of that code block it will
    # automatically call f.close()
    for line in f:
        print(line)
print()

# Read all the lines in one single list
with open('C:\\Users\\DELL\\PycharmProjects\\CodeBasics\\Data\\funny.txt', "r") as f:
    lines = f.readlines()
    print(lines)
print()

# To create a file
with open('C:\\Users\\DELL\\PycharmProjects\\CodeBasics\\Data\\love.txt', "w") as f:
    f.write("I love Python\n")
    f.write("I love meditation\n")

# If we do not want to overwrite and append the content, we use "a" mode which is append.
with open('C:\\Users\\DELL\\PycharmProjects\\CodeBasics\\Data\\love.txt', "a") as f:
    f.write("I love Go-lang\n")
    f.write("I love fruits")

# .writelines will take list as an input and every element in that list is a single line we want to write to Python file
with open('C:\\Users\\DELL\\PycharmProjects\\CodeBasics\\Data\\funny.txt', "w") as f:
    f.writelines([
        "I love C++\n",
        "I love scala"
    ])

# Find scores.csv file (05:42)
