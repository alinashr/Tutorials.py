# EXERCISE 3
# define a class and create object/instance


# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
class Person:
    counter=0   #class variable
    def __init__(self,age,height):
        # counter=counter+1
        # print("Constructor called")
        Person.counter+=1
            # print(counter)
        self.age=age
        self.height=height
    
    def o(self):
        print("Height:",self.height)
        print("Age:",self.age)

# counter=0
# print(counter)
p1=Person(21,5)
p2=Person(91,5)

print(p1.o())
print(Person.counter)
    
   


























