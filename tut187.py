# OOP Instanc  Methods
# Object and Instance are same thing

# OOP Instance Methods : Python tutorial 187
# all functions inside class --> Method


# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables 
        # print('init method(gets called by itself) / first constructor get called')
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return {f"{self.first_name}  {self.last_name}"}

p1=Person('ALINA','SHRESTHA',23)   #p1 and p2 are objects
print(p1.full_name())
# print(Person.full_name(p1))  --> Actually this  happens
