

# Filter function 

# adding even number to a new mt list  using normal conditions
# nums=[1,2,3,4,5,6,7,8,9,10]
# odd=[]
# for i in nums:
#     if i%2!=0:
#         odd.append(i)
# print(odd)

# adding even number to a new mt list  using filter function

def is_even(a):
    return a%2==0
numbers=[1,2,3,4,5,6,7,8,9,10]
#evens=tuple(filter(is_even,numbers))
evens=tuple(filter(lambda a:a%2==0,numbers))
print(evens)
    













