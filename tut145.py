# from inspect import Parameter
# kwargs (keyword arguments)
# **kwargs (double star operator)
# kwargs as a Parameter

def func(name,**kwargs):   #type of kwargs is dict
    for k,v in kwargs.items():
        # print(name)
        print(f"{k} : {v}")
    # print(kwargs)
    print(type(kwargs))

f=func('jkj',first='ali',last='shr')
#unpacking dictionary
# d = {'name':'jkjk','first':'ali','last':'shr'}
# print(d)
# print("\n")
# func(**d)
print(f)






