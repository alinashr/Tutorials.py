# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.

class laptop:
    dis_per=10
    def __init__(self,brandname,modelname,price):
        print('construcot-self called')
        self.brname=brandname
        self.mname=modelname
        self.price=price
    def apply_discount(self):
        return self.price-(laptop.dis_per/100)*self.price
laptop.dis_per=10
l1=laptop('lenovo','len454',55000)
l2=laptop('dell','dell0454',85000)
# l1.price=apply_discount(40)
print(l2.apply_discount())
# print(l2.brname)

print(l2.__dict__)








