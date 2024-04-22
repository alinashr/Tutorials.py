# advanced sorted function

# Normal sorting
# fruits=['apple','aalin','orange']
# fruits.sort()
# print(fruits)    --> lists can be sorted


fruits=('apple','aalin','orange')    # --> Tuples are immutable
print(sorted(fruits))
print(fruits)      #This clearly shows tuples are immutable

# fruits.sort()
# print(fruits)    --> tuples cannot be sorted   

student1=[
    {'name':'alina','score':90,'age':24},
    {'name':'alisa','score':45,'age':22},    #Example of dictionary inside list
    {'name':'rohit','score':49,'age':31}
]
print(sorted(student1,key=lambda item:item['score'], reverse=True))