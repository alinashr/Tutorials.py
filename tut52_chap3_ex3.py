# import numbers
# from unittest.util import three_way_cmp


# exercise one of three_
# sum of n natural numbers
# ask a user for natural number(n)
# print total from 1 to n


n=int(input("Enter a number upto which you want sum : "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1

print(sum)    
