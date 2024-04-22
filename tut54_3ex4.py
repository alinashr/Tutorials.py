# # from unicodedata import digit


# # problem
# # ask user to input a number containing more than one digit
# # example - 1256
# # calculate 1+2+5+6

# # algorithm-(method to solve problem in human language)
# # ask input in string , i.e don't change string to int
# # example= "1256"
# # pick string character one by one and change to int
# # int(example[0] + int(example[1])+.....go upto len(example)

# num=(input("Enter a number containing more than one digit : "))
# # num=int(num)
# print(num[0])
# len= len(num)
# print(len )
# sum=0
# # sum=num[0]+num[0]+num[0]+num[0]
# i=0
# while i<len:
#     sum = sum+int(num[i])
#     i+=1
# print("The sum of the digits of a number is : ")
# # print(sum)

# 


# \Second PRactise 
num=input("Enter number")
length=(len(num))
print(length)
i=0
sum=0
while i<length:
    sum=sum+int(num[i])
    i=i+1
print(sum)
