# import string

# num to string 
# define a function 

# example 
# input ----> [True, False, [1,2,3],]
# output ---> ['1','2','3']

list=[1,2,3,"d",True]

def fun(l):
    return [str(i) for i in l if (type(i)== int or type(i)==float )]
print(fun(list))



