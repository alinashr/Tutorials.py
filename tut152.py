# We use enumerate function with for loop to track position of our item in iterable 

# # How we can do this without enumerate function 
# import string


names = ['abc','abcdef','harshit']
# pos=0
# for name in names:
#     print(f"{pos} ---> {name}")
#     pos=pos+1

# with enumerate function   

for pos,name in enumerate(names):
    print(f"{pos} ---> {name}")

# Define a function that take two arguments 
#  1.) list containing string
#  2.) string that want to find in your list
#  and this function will return the index

# pos=0
# def find_pos(l,target):
#     for pos,name in enumerate(l):
#         if name==target:
#             return pos
#     return -1      
# print(find_pos(names,'adef'))
# print(find_pos(names,'abc'))



# name=[1,2,3]
# pos=0
# for n in name:
#     print(f"{pos}:{n}")
#     pos+=1

#repracticing
# Define a function that take two arguments 
#  1.) list containing string
#  2.) string that want to find in your list
#  and this function will return the index
# num=['alinssa','alina','shr','stree']
# n='alina'
# pos=0
# for n in enumerate(num):
    
#     print(f"{pos}")

names=['alina','alisa','melisa']
def func(l,target):
    for pos,name in enumerate(l):
       if name==target:
          return pos
    return -1
   
print(func(names,'melisa'))











