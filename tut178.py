def nums(n):
    for i in range(1,n+1):
        yield(i)

# print(nums(7))
numbers=(nums(10))   #genarator
for number in numbers:
    print(number)
for number in numbers:
    print(number)

# for number in nums(10):
#     print(number)
# for number in nums(10):
#     print(number)


















