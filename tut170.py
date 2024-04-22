# decorators part- II


def decorator_function(any_function):
    def wrapper_function(*args,**kwargs):
        print('This is amazing')
        any_function(*args, **kwargs)     #calls func2
    return wrapper_function

@decorator_function
def func(a):
    print(f"This is function with argument {a}")

@decorator_function
def add(a,b):
    return a+b
print(add(3,6))
# func(7)
 