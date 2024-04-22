#adding and delete data from dictionary

user_info = {
    'name' : 'alina',
    'age':21,
    'fav_movie'  : ['Xyz','abc'],
    'fav_songs': ['fairy tale','guitar'],
}

# #add data
user_info['fav_song']=['sanam re','lukachhupi']
print(user_info)

#removing data using 
# pop method
popped_item = user_info.pop('fav_movie')
print(f"popped_ite  is {popped_item}" )  #string formatting

# print(user_info)

#popitem method for deleting random key value
popped_item = user_info.popitem()
print(user_info)
print(f"popped_item is {popped_item}")  #OUTPUT -> popped_item is ('fav_songs', ['fairy tale', 'guitar'])
print(type(popped_item))
# print(type(user_info))
