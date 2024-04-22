# practice for loop
# ask user a number like 3444
# calculate the sum of digits ---> 3+4+4+4


num=input("Enter digit of your choice: ")
len=len(num)
# print(len)
i=0

total=0
# for i in range(len):
#     total=total + int(num[i])
 
# print(total)

for i in  num :
    total=total + int(i)
    
 
print(total)