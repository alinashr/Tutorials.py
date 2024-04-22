# OOP CLASS METHODS:

# class methods & instance methods -> Difference

# we use class methods less frequently than instance methods


# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
class Person:
    counter=0   #class variable
    def __init__(self,age):
        # counter=counter+1
        # print("Constructor called")
        Person.counter+=1
            # print(counter)
        self.age=age
        # self.height=height
    
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.counter} instances of  {cls.__name__} class."
    def o(self):
        print("Height:",self.height)
        print("Age:",self.age)

# counter=0
# print(counter)
p1=Person(21)
p2=Person(91)
print(p1.count_instances())

# print(p1.o())
# print(Person.counter)
    
   





























