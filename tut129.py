#CHAPTER 9 EX-1
# define a function that take list of Strings 
# list containing reverse of every string


# Note - USE LIST COMPREHENSION because we already did this exercise 
#using normal method

# Example
# l = ['abc','jff','dfd']
# rev_string(l) ----> ['cab','ffj','dfd']
# l = ['abc','jff','dfd']
# rev_list=[]
# for i in l:
#     rev_list.append(i[::-1])
# print(rev_list)

#using LIST COMPREHENSION method 
l = ['abc','jff','dfd']
rev_list2=[i[::-1] for i in l]
print(rev_list2)



#OTHER EXAMPLES
#using simple method creating list of reversed items of fruit
# fruits=['Orange','Apple','Grapes']
# rev_fruit=[]
# for fruit in fruits:
#     rev_fruit.append(fruit[::-1])
# print(rev_fruit)

#using LIST COMPREHENSION method creating list of reversed items of fruit
# fruits=['Orange','Avocao','Grapes']
# rev_fruit2=[fruit[::-1] for fruit in fruits]
# print(rev_fruit2)
