
# take two comma separated inputs 
# from user_input
# 1) user's name
# 2) a single CharacterData

# output - 2 print lines
# 1) user's name length 
# 2) count the character that user inputed(bonus: case insensitive count)

# name,char=input("Enter name and the character: ").split(",")
# print(f" User name length is {len(name)}")
# print(f"and no of character is {name.count(char)}") #case sensitive that is a and A are different
# print(f"character count : {name.lower().count(char.lower())}") #case insensitive
# x=name.strip().lower().count(char.strip().lower())
# print(x)
# char.strip().lower()      

# $ python chap2ex3_tut31.py
# Enter name and the character:     Alina,a
#  User name length is 9
# and no of character is 1
# character count : 2   
x="real estate marketing agency"     
print(x.title())  


