# python tut83addtolist.py
#more methods of adding data to the list using append and insert method
# adding data to the list using append which add to the end of the data 
#concatening two lists using '+' 
# from operator import methodcaller
#  


colour=[]
colour.append("YEllow")     #only one data is appended using this
colour.append("Red")
colour.append("Black")
# colour.insert(1,"orange")
print(colour)
fruit1=["grapes","orange","apple"]
fruit2=["mango","banana"]
# fruit=fruit1+fruit2
# print(fruit)
# fruit1.extend(fruit2)
fruit1.append(fruit2)
print(fruit1)

fruit1=["app","bana"]
fruit1.insert(1,"pine")
print(fruit1)
fruit2=["or","litch"]
# fruit=fruit1+fruit2
# print(fruit)
fruit1.extend(fruit2)
print(fruit1)
