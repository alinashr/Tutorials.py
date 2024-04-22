#fromkeys,__get,__copy,__clear methods

# d={'name': 'unknown', 'age' : 'unknown'}

        # d = dict.fromkeys(['name','age','height'],'unknown')   #creating dicntionary
        # print(d)

# d = dict.fromkeys("str",'unknown')

# we can also use range function 
# d = dict.fromkeys(range(1,11),'unknown')
# print(d)

#get method(useful)
d = {'name': 'alina','age': 22}
# print(d['names'])
print(d.get('name'))
print(d.get('age'))

# if 'name' in d:
#     print("YEs present")

# else:
#     print("Not present")


# if d.get('name'):
#     print("YEs present")

# else:
#     print("Not present")

#clear method
# d.clear()
# print(d)

#copy method
# d1=d.copy()   
# print(d1 == d)
        #   Output
        #   ('height', 'unknown')
        #   {'name': 'unknown', 'age': 'unknown'}
        #   {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}
           
# print(d)
# d1=d 
        #{'name': 'unknown', 'age': 'unknown'}
        #{'name': 'unknown', 'age': 'unknown'}

# print(d1.popitem())
# print(d1)
# print(d)

# print("\n")



