from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper_func(*args, **kwargs):
        if all([type(arg) == int for arg in args]):
            return function(*args, *kwargs)
        print("Invalid arguments")
        
             # data_types=[]
        # for arg in args:
        #     data_types.append(type(arg)==int)
        # if all(data_type):
        #     return function(*args, **kwargs)
        # else:
        # 
        #     print("Invalid arguments") 
    return wrapper_func

@only_int_allow
def add_all(*args):
    # @wraps(function)
    # def wrapper(*args, **kwargs):
    total=0
    for i in args:
        total+=i
    return total

print(add_all(4,5,6))




