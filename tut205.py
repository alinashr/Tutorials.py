# Error raise example 1 : Python tutorial 205
#NOtImplementedError
#abstract Method

class Animal:
    def __init__(self,name):
        self.name=name
    
    #abstract method if from java programming lang
    #there is no anything like abstract in python

    def sound(self):
        return NotImplementedError('you have to define this mehtod in subclasses')
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    # def sound(self):
    #     return ('bhau bhau')
    

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return ('meow meow')
        
    

dog=Dog('Michael','Belayeti')
cat=Cat('Ganga','Bhi')

print(dog.sound())
print(cat.sound())