x=12     #global variable

def sum():
    global x    #modyfying global variable data
    x=8         #local  variable
    return x


print(x)
print(sum())
print(x)