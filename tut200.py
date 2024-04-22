# Multilevel inheritance ,
# MRO(Method Resolution Order) , 
# Method Overriding : Python tutorial 200
#isinstance(),issubclass()  --> built-in func


# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
class Phone:
    def __init__(self,brand, model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    # def full_name(self):
    #     return f"{self.brand} {self.model_name}"
    def full_name(self, color):
        return f"{self.brand} {self.model_name} "
    def make_a_call(self,number):
        return f"Calling {number}....."
    
class Smartphone(Phone):    #inheriting fone cls
    def __init__(self, brand,model_name, price, ram, internal_memory, rear_camera):
        # Phone.__init__(self,brand,model_name, price)
        super().__init__(brand,model_name, price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"
    def make_a_call(self,number):
        return f"Calling {number}.....to xyz"  #This will overide the previous method
class Smartphone2(Phone):    #inheriting fone cls
    def __init__(self, brand,model_name, price, ram, internal_memory, rear_camera):
        # Phone.__init__(self,brand,model_name, price)
        super().__init__(brand,model_name, price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
    # def full_name(self):
    #     return f"{self.brand} {self.model_name}"
    # def make_a_call(self,number):
    #     return f"Calling {number}....."

class FlagshipPhone(Smartphone):
        def __init__(self, brand,model_name, price, ram, internal_memory, rear_camera,chargertype):
            super().__init__(brand,model_name, price,ram, internal_memory, rear_camera)
            self.chargertype=chargertype
        def full_name(self):
          return f"{self.brand} {self.model_name} and price is {self._price} also {self.rear_camera}"



phone=Phone('nokia','1100',1000)
# print(phone.full_name())

print(phone.full_name("red"))
# print(phone.full_name())

smartphone=Smartphone2('redmi','11',23000,'8 gb','128 gb','40mp')
# print(phone.full_name())
onep=FlagshipPhone('redmi','11',23000,'8 gb','128 gb','40mp','TYPE_C')
print(onep.full_name())
# print(smartphone.full_name()+f" and price is {smartphone._price}")
# print(onep.full_name()+f" and price is {onep._price} having charger {onep.chargertype}")
# print(help(FlagshipPhone)) 
print(onep.make_a_call(987877888))
# print(isinstance(onep,Phone))

print(issubclass(FlagshipPhone,Smartphone))