#chap 5 ex - 6
# last exercise of this chapter

#function takes input as [[1,2,3],[1,2]] and return no of  lists inside list
#type() is used to check

# num=[1,2,3,[4,5,6]]
# def in_num(n):
#     counter = 0
#     for i in n:
#         if type(i)==list:
#             counter+=1
#     return counter

# print(in_num(num))


# lit=[1,2,3]
# def no(lit):
#     c=0
#     for i in lit:
#         if type(i)==list:
#             c=c+1    #counts no of lists within lists
#     return c
# print(no(lit))














liss=[1,2,3,[3,4],[3,5],[1]]
def cpim(liss):
    count=0
    for i in liss:
        if type(i)==list:
            count=count+1
    return count

print(cpim(liss))












