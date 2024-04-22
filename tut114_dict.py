# dictionaries Intro 
# Q-n) Why we need dictionaries 
# Ans: Because of limitations of lists, lists are not enough to represent real data 

# What are dictionaries? 
# Unordered collections of data in key: value pair 

#how to create dictionaries 
# user = {'name': 'Alina', 'age' : 21 }
# print(user)

# print(type(user))

# print(user['name'])

# print(user[1]) There's no anything like indexing in dictionaries

#second method to create a dictionary
user1 = dict(name = 'Alina', age = 24)
#accessing data from dictionary
print(user1['name'])
print(user1['age'])

#Which type of data a dictionary can store?
#anything it can be numbers, strings,list, dictionary

#modeling 
user_info = {
    'name' : 'alina',
    'age':21,'fav_movie'  : ['Xyz','abc'],
    'fav_songs': ['fairy tale','guitar'],
}
print(user_info['fav_songs'])

#how to aadd data to empty dictionary
# user_info2 = {}
# user_info2['name']='alina'
# user_info2['age']=21
# print(user_info2)
# liss=[1,2,3]
# tupp=[1,23,4]
# print(liss[0])
# print(tupp[0])



# Define the user1 dictionary
# user1 = dict(name='Alina', age=24, salary=290000)

# Access the 'name' key
# name = user1['name']
# print(user1['name'])  # Output: 'Alina'

# Access the 'age' key
# age = user1['age']
# print(user1['age'])  
# Output: 24
# print(user1['salary']) 

user_infoo={

}

user_infoo['name']='Alna'
print(user_infoo)    #this creates dictionery



# You can also use the keys() and values() methods to get a list of keys or values, respectively:
# Define the user1 dictionary
user2 = dict(name='Alina', age=24)

# Access all the keys in the dictionary using the keys() method
keys = user2.keys()
print(keys)  # Output: dict_keys(['name', 'age'])

# Access all the values in the dictionary using the values() method
values = user2.values()
print(values)  # Output: dict_values(['Alina', 24])
