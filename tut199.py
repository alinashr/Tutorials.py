# inheritance Intro : Python tutorial 


# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
class Phone:
    def __init__(self,brand, model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def make_a_call(self,number):
        return f"Calling {number}....."
    
class Smartphone(Phone):
    def __init__(self, brand,model_name, price, ram, internal_memory, rear_camera):
        # Phone.__init__(self,brand,model_name, price)
        super().__init__(brand,model_name, price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def make_a_call(self,number):
        return f"Calling {number}....."
phone=Phone('nokia','1100',1000)
smartphone=Smartphone('redmi','11',23000,'8 gb','128 gb','40mp')
print(phone.full_name())
print(smartphone.full_name()+f" and price is {smartphone._price}")