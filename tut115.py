# #looping and in keyword


# #in keyword
user_info = {
    'name' : 'alina',
    'age':21,
    'fav_movie'  : ['Xyz','abc'],
    'fav_songs': ['fairy tale','guitar'],
}

# # check if key exist in a dictionary
# if 'name' in user_info:   #for checking key only in the dictionary
#     print("present")
# else:
#     print('not present')

#for checking key only in the dictionary
# if 'name' in user_info.keys():   
#     print("present")
# else:
#     print('not present')

# #for checking values only in the dictionary
# if 'alina' in user_info.values():   #for checking values only in the dictionary
#     print("present")
# else:
#     print('not present')   

# # check if value exist in a dictionary
# if  'na' in user_info.values():
#     print("present")
# else:
#     print('not present')


# #Loops in dictionary 

# #for keys
# for i in user_info:
#     print(i)

# print("\n")
# #for values
# for i in user_info.values():
#     print(i)
# print("\n")

#values method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))


for i in user_info:
    print(user_info[i])    #prints all values

# for i in user_info:
#     print(i)     #prints all keys 

# print("\n")
# for i in user_info.values():
    
#     print(i) 


# items method
user_items = user_info.items()
print(user_info.items())
print(type(user_items))
# 
# print(user_info.items())   THis is called commenting
# for key,value in user_info.items():
#     print(f"key is {key} and value is {value}")



















