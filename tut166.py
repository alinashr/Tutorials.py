

# Pass Function as argument
# map

def square(a):
    return a**2
l=[1,2,3,4]
def my_map(funct, l):
    new_list=[]
    for item in l:
        new_list.append(funct(item))
    return new_list

print(my_map(square,l))
print(my_map(lambda a:a**3,l))



