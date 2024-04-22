# make flexible functions 
# *operator   ---> solves problem of multiple addition in function 
# *args 

def total(a,b):
    return a+b

print(total(3,4))

def all_total(*args):      #args is used becautuse it is conventional
    sum=0
    for i in args:
        sum+=i
    print(sum)

print(all_total(3,4))
