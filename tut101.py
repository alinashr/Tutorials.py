
#chap 5 ex 4


# filter odd even 
# define a function 
# input 
# list --> [1,2,3,4,5,6,7]

# output ----> [[1,3,5,7],[2,4,6]]

# def list_num(n):
#     odd_num = []
#     even_num = []
#     for i in n:
#         if i%2 ==0:
#             even_num.append(i)
#         else:
#             odd_num.append(i)
#     output = [odd_num,even_num]
#     return output


# num=[1,2,3,4,5,6,7]
# l = list_num(num)
# print(l)


# filter odd even 
# define a function 
# input 
# list --> [1,2,3,4,5,6,7]

# output ----> [[1,3,5,7],[2,4,6]]


# Repractise


list=[1,2,3,4,5,6]
def df(list):
    even=[]
    odd=[]
    for i in list:
        if i%2==0:
            even.append(i)
            
        else:
            odd.append(i)
    output = [odd,even]
    return output
            
l=df(list)
print(l)