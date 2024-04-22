#more about sets

# s={'a','b','c','d','e'}
s={1,2,3,4}

for x in s:
    print(x)

if 7 in s:
    print("Yes present")

else:
    print("Not present")

# for item in s:
#     print(item)

s1={1,2,3,4}
s2={3,4,5,6}
# print(s1.union(s2))  -> same as union=s1|s2
# print(s1.intersection(s2))   -> same as intersection=s1&s2
union=s1|s2
intersection=s1&s2
print(union)
print(intersection)



