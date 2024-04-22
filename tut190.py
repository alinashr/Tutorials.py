# Class Variable : Python tutorial 190
# Class VariableEXAMPLE NO.1

class circle:
    pi=3.14  #class variable
    def __init__(self,radius):
        self.radius=radius
    def calc_circum(self):
        return 2*circle.pi*self.radius

c=circle(3)
print(c.calc_circum())

# Class VariableEXAMPLE NO.2 --> apply discount on sale and remove discount after sale is finished

class laptop:
    dis_per=10
    def __init__(self,brandname,modelname,price):
        print('construcot-self called')
        self.brname=brandname
        self.mname=modelname
        self.price=price
    def apply_discount(self,dis):
        return self.price-(dis/100)*self.price
# laptop.dis_per=0
# l1=laptop('lenovo','len454',55000)
l2=laptop('dell','dell0454',40000)
# l1.price=apply_discount(40)
print(l2.apply_discount(40))
# print(l2.brname)

print(l2.__dict__)






