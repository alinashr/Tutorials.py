# list vomprehension in nested list 

# example = [[1,2,3] , [1,2,3] , [1,2,3]]

# Using Nested list comprehension
nested_comp = [ [ i for i in range(1,4)] for j in range(3)]
print(nested_comp)

# Using simple method 
newlist = []
for j in range(4):
    newlist.append([1,2,3])

print(newlist)

#tut137
#revision
#list of square of digits from 1 to 10
# sq=[]
# for i in range(1,11):
#     sq.append(i*i)

# print(sq)

sqw=[i for i in range(1,11) if i%2!=0]
print(sqw) 

