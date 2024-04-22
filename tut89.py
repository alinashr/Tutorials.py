# from operator import methodcaller


# Split method 
# convert string to list 

user_info = 'harshit;24'.split(";")
print(user_info)
name,age='harshit,24'.split(',')
print(name)
print(age)

print("\njoin method")
# join method 
# convert list to string

user_info = ['23','45']
print(','.join(user_info))