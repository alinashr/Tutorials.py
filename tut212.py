# Python Debugger

# Debugger is nothing but to find the errors and to fix it.

# So, why debugging?
# Our program is not running and causing unexpected errors.
# Our program is working fine but not working as we want.


import pdb
pdb.set_trace()
name=input('Please type your name : ')
age=int(input('Please type your age : '))
age1 = age+5
print(f'{name} will be {age1} in next five years.')

#commands -> l,n,q,c(continue)

