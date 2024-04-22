# Raise errors : Python tutorial 204

def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    return TypeError('Oopf you have passed wrong data type to function')

    
print(add('1','2'))




