# # Advance min() and max()
# p=[1,2,4,5]
# print(min(p))


names=['Alina','Shresthadddddddd','dke','d','Aldfndherty']
# def func(item):
#     return len(item)
# print(max(names,key=func))

# Using lambda function
# print(max(names,key=lambda i:len(i)))
#Examples of dictionary
students={
    'alina':{'score':90,'age':24},
    'alisa':{'score':45,'age':22},     
    'rohit':{'score':49,'age':31}

}
print(max(students,key=lambda item:students[item]['age']))
student1=[
    {'name':'alina','score':90,'age':24},
    {'name':'alisa','score':45,'age':22},    #Example of dictionary inside list
    {'name':'rohit','score':49,'age':31}
]
# print(max(student1,key=lambda item:item.get('age'))['score'])







