'''ssddddds '''

from functools import wrap

def decorator_function(any_function):
    def wrapper_function(*args,**kwargs):
        print('This is amazing')
        any_function(*args, **kwargs)     #calls func2
    return wrapper_function

@decorator_function
def add(a,b):
    ''' this is add function '''
    return a+b

print(add.__doc__)
print(add.__name__)


# import matplotlib
# import functools
# print(functools.file)