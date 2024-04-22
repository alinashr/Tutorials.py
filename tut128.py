# from pdb import line_prefix

# list comprehensive
# with the help of list comprehension we can create list in one line_prefix

# create a list of squares from 1 to 10
#simple method
# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

#creating list with list comprehension
# square2=[i**2 for i in range(1,11)]
# print(square2)


#create a list of negative list 
#simple method
# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)


#create a list of negative list using "list comprehension"
negative2=[-i for i  in range(1,11)]
print(negative2)

#printing first letter of the items in list using simple method
names =  ['Alina','Salina','Nila']
# newlist = ['A','S','N']
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print(new_list)

#printing first letter of the items in list using "list comprehension"
names =  ['Alina','Salina','Nila']
new_list2=[name[0] for name in names]
print(new_list2)


