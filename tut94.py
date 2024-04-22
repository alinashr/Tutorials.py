# from operator import methodcaller


# generate lists with range functions 
# something more about pop method 
# index method 
# pass list to a function 


numbers = list(range(1,21))
# print(numbers)
# pr=numbers.pop()
# print(pr)

# print(numbers.index(3))

# def neg_list(l):
#     negative=[]
#     for i  in l:
#         negative.append(-i)
#     return negative

# print(neg_list(numbers))

# n=[1,3,5,6,8,7,6,3,2]
# print(n.index(3,7,8))


# print 2,4,6,8,10
n=[1,2,3,4,5]
def mul_two(list):
    mul=[]
    for i in list:
        mul.append(2*i)
    return mul
print(mul_two(n))