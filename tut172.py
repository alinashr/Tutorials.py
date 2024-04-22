from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"You are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function("*args, **kwargs")
    return wrapper

@print_function_data
def add(a,b):
    '''THis function takes two numbers as arguments and return thir sum'''
    return a+b

# add(3,1)








