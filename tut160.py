# all and any function->true or false

num1=[2,4,6,8,9]
num2=[3,1,7,5]

# even=[]
# for num in num1:
#     if num%2==0:

#         print(even.append(num))
#     # even.append(num%2==0)
# print(even)
even=[num if (num%2==0) else print() for num in num2]
print(even)
print(any(num%2==0 for num in num1)) 





