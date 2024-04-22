# Closures practice or function returning function practice

#square
#cube


def to_power(x):   #x=3
    def calc_power(n):    #n=2
        return n**x 
    return calc_power

cube = to_power(4)
print(cube(2))
# print(to_power(3))