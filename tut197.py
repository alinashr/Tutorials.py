# Encapsulation, Abstraction, Naming Convention, Name Mangling : Python tutorial 197


# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
class Person:
    counter=0   #class variable
    def __init__(self,age,height):    # age,height -> THese are the instant variables
        Person.counter+=1
        self.age=age
        self.__height=height
    def o(self,salary):
        print(f"Calling {salary}")

    # def send():
    #     pass
p1=Person(21,5)
print(p1.__dict__)    


# print(p1._height)/
# p1._height=-5
# print(p1._height)


# print(p1.o(23000))

# Abstraction
# l=[7,9,4,1]
# l.sort()     #tim sort
# print(l)   #
# print(Person.send())

# Naming Convention
# _name -> Convention of private name   -> shows to the developer that this is private

#Name Mangling
# __name__ -> double underscore(dunder) / magic methods
