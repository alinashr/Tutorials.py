# OOP EXERCISE 2 : Python tutorial 188
# l1.apply_discount(40)  -> applies 40% to the pric of laptop

class laptop:
    def __init__(self,brandname,modelname,price):
        print('construcot-self called')
        self.brname=brandname
        self.mname=modelname
        self.price=price
    def apply_discount(self,discount):
        return self.price-(discount/100)*self.price
l1=laptop('lenovo','len454',55000)
l2=laptop('dell','dell0454','85000')
# l1.price=apply_discount(40)
print(l1.apply_discount(100))
# print(l2.brname)
