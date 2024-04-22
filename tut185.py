# oop exercise 1:
# create a laptop class with attributes like brandname, model name, price
# create two objects/instance of your laptop class


# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
class laptop:
    def __init__(self,brandname,modelname,price):
        print('construcot-self called')
        self.brname=brandname
        self.mname=modelname
        self.price=price

l1=laptop('lenovo','len454',55000)
l2=laptop('dell','dell0454','85000')
print(l1.price)
print(l2.brname)