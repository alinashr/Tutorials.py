#Iterator vs Iterable


num=[1,2,3,4,5]  #list, tuples --> iterables
sq=map(lambda a:a**2,num)
# xx=iter(num)
# print(xx)
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))

