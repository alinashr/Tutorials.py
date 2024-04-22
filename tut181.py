

# square=[i**2 for i in range(1,11)]
# print(square)   --> List Comprehension

# Generator comprehension
square=(i**2 for i in range(1,11))
# yield(square)
for num in square:
    print(num)
    
for num in square:
    print(num)
