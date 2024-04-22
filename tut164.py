# More about functions

# what are doc strings
# how to write docstrings 
# how to see docstring
# what is help function

def add(a,b):
    ''' this function takes 2 numbers and return their sum'''

    return a+b
# print(add(2,3))
print(add.__doc__)
# print("JEllo")

#DOCSTRING
#  function that we have discussed till now
# len, sum, max, min, sorted  -> already defined in python
def lent(a):
    '''HEllo'''
    return len(a)
print(lent('alina'))
# print(lent.__doc__) #if we want to read the docstring of the len function
# print(len.__doc__)
# print(sum.__doc__)
print(help(sum))

