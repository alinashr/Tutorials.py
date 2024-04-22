#defaf"lt parameters

def display(name,age,roll=22):
    print(f"My name is {name}")
    print(f"My age is {age}")
    print(f"My roll is {roll}")


display("alina",21,4)

#default parameter
def sum(x,y,z=2):    #x,y,z are all parameters and z is default parameter which should be at last
    sum=x+y+z
    return sum
print(sum(2,3))    #2 and 3 are arguments
