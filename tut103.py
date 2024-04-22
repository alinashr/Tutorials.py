
# common elements finder function 
# define a functions which take 2 lists as input and return a list which contains elements of both list_dialects

# example 
# input ---> [1,2,3,4] , [2,3,6,7]
# output ----> [1,2]




def common_num(a,b):
    to = []
    for i in a:
        if i in b:
            to.append(i)
    return to

    

num1=[1,2,3,4]
# print(num1[2])
num2=[3,2,6,7]
print(common_num(num1,num2))


# num1=[1,2,3,4,5]
# num2=[2,4,5,6,7,8]

# def common(num1,num2):
#     cm=[]
#     for i in num1:
#         for j in num2:
#             if i==j:
#                 cm.append(i)
#     return cm

# print(common(num1,num2))