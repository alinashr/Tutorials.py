# tut126_set.py

# set data type 
# unordered collection of unique items

s={1,2,'a',2,7,4}
# print(s[1])     cannot be indexed

l=[1,9,9,9,8,7,7]

sett=set(l)
print(sett)
print(list(set(l)))

#different methods in set
s.add(11)
print(s)
s.remove(1)   #show error when the choosen elemnt is not present in thr set
s.discard(8)  #show no error when the choosen elemnt is not present in thr set and remoed when the element present
print(s)



#copy in set
s1=s.copy()
print(s1)
s.clear()
print(s)
 