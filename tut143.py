# define a function 
# input 
# num, iterable(tuple,list) containing numbers as Args

# example 
# nums = [1,2,3]
# to_power(3,*nums)

# Output 
# list ---> [1**3, 8 , 27]

# if user did't pass any args then give a user a message 'hey you didn't pass args
# else 
#    return list
# Use list comprehension 

nums=[1,3]
def to_power(num,*args):    
    if args:
        return [i**num for i in args]    #list comprehension
    else:
        return "you didn't pass args"

print(to_power(3,*nums))     













































































































































