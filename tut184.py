# creating my first class in Python
# from datetime import date

# tomorrow = date.tomorrow()
# print("Today's date:", tomorrow)
# # Today's date: 2024-02-04
# Explain
# import datetime import date
# today = date.today()
# yesterday = today - datetime(days = 1)
# tomorrow = today + datetime(days = 1) 
# print('Yesterday : ',yesterday)
# print('Today : ',today)
# print('Tomorrow : ',tomorrow)

# what is class, how to create, itit method/constructor 
# what is , attributes, instance variables
# how to create our object?


# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables 
        print('init method(gets called by itself) / first constructor get called')
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person('ALINA','SHRESTHA',23)   #p1 and p2 are objects
# p2=Person('ALIshan','SHRESTHA',19)
print(p1.first_name)
print(p1.last_name)
