#more about get 

d={'name': 'unknown', 'age' : 32,'age':22}
print(d.get('name'))
#if the key is not found then it returns none like when { print(d.get('names')) --> None }
print(d)    #override the value by 22

d={'name': 'unknown', 'age' : 22,'age':32}
print(d)