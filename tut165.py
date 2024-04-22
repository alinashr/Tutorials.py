#DECORATORS
'''
You have to have a complete understanding of functions,
first class function/closures
then finally we will learn about decorators
'''

# As stated above the decorators are used to modify the behaviour of function or class.
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

# print("HEllo")

def square(a):
    return a**2
s=square

print(s(7))
#Here s and sqaure are same
def p():
    exit
print(s.__name__)
print(square.__name__)
# print(s)
# print(square)
print(p)
