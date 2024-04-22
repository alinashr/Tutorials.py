# Special magic/dunder method, operator overloading, polymorphism : Python tutorial 202
#dunder-> double underscore

# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def phone_name(self):
        return f"{self.brand} {self.model}"
    #str, repr
    def __str__(self):
        return f'{self.brand} {self.model}'
    def __repr__(self):
        return f'Phone(\'{self.brand}\',\'{self.model}\',\'{self.price}\')'
    def __len__(self):
        return len(self.phone_name())
    def __add__(self,other):
        return self.price * other.price

class Smartphone(Phone):
    def __init__(self,brand,model,price,camera):
        super().__init__(brand,model,price)
        self.camera=camera
    def phone_name(self):
        return f"{self.brand} {self.model} is worth Rs.{self.price}"

myphone=Phone('nokia','n201',22)

#prints the location of object in memory
# print(str(myphone))
# print(len(myphone))
# print((myphone))

# print(repr(myphone))
# print(myphone.__repr__())

# operator overloading
#2+3=5
# 'abc'+'def'='abcdef
myphone2=Phone('lg','lg201',22000)
mysmartphone=Smartphone('Redmi','R100',45000,'16 MP')
print(myphone.phone_name())

print(mysmartphone.phone_name())
# k=myphone+myphone2
# print(k)
# print(myphone.__add__(4))

# polymorphism
#operator overloading is the example of polymorphism

