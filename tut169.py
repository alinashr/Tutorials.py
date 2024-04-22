# Decorators enhance the functionality of other functions

def decorator_function(any_function):
    def wrapper_function():
        print('This is amazing')
        any_function()     #calls func2
    return wrapper_function

 

#This is amazing
def func1():
    print('this is function 1')

#This is amazing
def func2():
    print('this is function 2')
# func1()
# func2()

var=decorator_function(func2)
var()






