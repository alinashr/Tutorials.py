# function with all types of parameters

# default parameters
# def func(name='akf',age='21'):
#     print(name)
#     print(age)


# print(func())
# PADK   p=> parameter, A=star arg , Default parameters, Kwargs
def all_type(name,*args, last_name='shrestha',**kwargs ):
    print(name)
    print(last_name)
    print(kwargs)
    print(args)

all_type('alina',1,2,3,4,sex='Female',age=22)