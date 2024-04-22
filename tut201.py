# Multiple Inheritance : Python tutorial 201

class A:
    def class_a_method(self):
        return 'I\'m just a class A method'
    # def hello(self):
    #     return 'hello from class A'
    
class B:
    def class_b_method(self):
        return 'I\' just a class B method'
    def hello(self):
        return 'hello from class B'
    
class C(B,A):
    pass

instance_c=C()
# print(instance_c.class_a_method())
# print(instance_c.class_b_method())
# print(instance_c.hello())

# method resolution order(MRO)- ways
#1)  print(help(C))   #helps to find method resolution order(MRO)
# 2)print(C.mro())
# 3)print(C.__mro__)

#Output
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]









