# list comprehension with if statment 

numbers = list(range(1,11))
#aim-> even_nums=[2,3,6]

# using simple method
# nums=[]
# for i in numbers:
#     if i%2==0:
#         nums.append(i)
# print(nums)

#using list comprehension

numbers = list(range(1,11))
even_num=[i for i in numbers if i%2==0]
print(even_num)
odd_num=[i for i in numbers if i%2!=0]
print(odd_num)


