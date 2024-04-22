#Summary of chapter 6 of TUPLE
'''
tuples are immutable 
tuples are ordered collections of items
tuples can store any data type
you cannot change(add or delete) values from tuple once it created
but can add, delete data from list which is present inside tuples
'''

mixed = (1,2,3,3,5)
#cannot be append, no pop, no insert , no remove
#only count index
print(mixed.count(3))
print(mixed.index(5))

#functions min() max()
# print(mixed.max())
# print(mixed.min())
#sum
#len

def diff_num(n):
    m=min(n)
    ma=max(n)
    l=len(n)
    s=sum(n)

print(diff_num(mixed))


