# take two comma separated inputs from user 
# 1) user's name, example - "Alina"
# 2) a single character, "H"

# output - 2 print lines
# 1) users name length
# 2) count the character that user inputed(case insensitive count)

name,char=input("Enter name and char to count").split(",")
print(f"The length of your name is {len(name)}")
print(f"THe no of char that you inputed in name is {name.lower().count(char)}")

