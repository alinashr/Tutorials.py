# ask user the key values and add the key and values into the dictionary

#printing format
# users ={
#     'name' : 'Alina'
#     'age'  : 24
#     'fav_movies' : ['Jab we met','Kal ho n ho']
#     'fav_songs' : ['Tum bin','mere humsafar']
# }

#now
user = {}
name = input("Enter your name")
age = input("Enter your age")
fav_movies = input("Enter your fav movie :").split(',')
fav_songs= input("Enter your fav songs").split(',')


user['name']= name
user['age']= age
user['fav_movies']= fav_movies
user['fav_songs']= fav_songs

for key,value in user.items():
    print(f"{key} : {value}")
    


