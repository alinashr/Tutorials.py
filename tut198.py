# OOP : Property and setter decorator : Python tutorial 198
#  the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation


# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
class Person:
    counter=0   #class variable
    def __init__(self,age,height):    # age,height -> THese are the instant variables
        Person.counter+=1
        self.age=max(age,0)

        self._height=max(height,0)
    @property    
    def height(self):
        print(f"Calling {self._height}")
    @height.setter    
    def height(self,nh):
        self._height=max(nh,0)
    #gettern and setter property
    
p1=Person(-21,-5)
print(p1._height)
p1._height=-100
print(p1._height)

# p1.heightt
# print(p1.age)
# print(p1.o)    #when used property decorator, we can call the function without the parenthesis