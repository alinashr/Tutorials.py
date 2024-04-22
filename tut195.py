# Class Method as a constructor : Python tutorial 195


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
    @classmethod
    def from_string(cls,string):
        age,height=string.split(',')
        return cls(age,height)

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.counter} instances of  {cls.__name__} class."
    
    #instant method
    def o(self):
        print("Height:",self.height)
        print("Age:",self.age)
    
    #instant method
    def fullinfo(self):
        return f"{self.age}years old {self.height}\""

# counter=0
# print(counter)
p1=Person(21,5)
p2=Person(91,4)
p3=Person.from_string('32,8')
# print(p3())
# print(p1.count_instances())

print(p3.__dict__)
print(p3.fullinfo())








