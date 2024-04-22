# *args with normal parameter  

def multiply_nums(num1,num2,*args):
    multiply=1
    print(num1 +num2)
    print(args)
    for i in args:
        multiply *=i
    return multiply

print(multiply_nums(2,2,4,9,3))
# print(multiply_nums(2,2))