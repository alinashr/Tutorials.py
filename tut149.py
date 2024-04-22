
def func(name,*args, last_name='shrestha', **kwargs):
    print(name)
    print(args)
    print(last_name)

    print(kwargs)
func("Alina",1,2,3,4,5,6,a=1,b=2)