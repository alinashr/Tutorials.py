#Exercise 1 of chapter dictinary
# define a functin that takes a nummber(n)
# returns a dictionary containing cube of numbers from 1 to n
# from 1 to N

# example 
# cube_finder(3)
# {1:1,2:8,3:27}

def fun(n):
    cubes={} 
    for i in range (1,n+1):      #key = i
        cubes[i]=i**3    #adding key i and value i**3 to the dictionary cubes
        i=i+1
    return cubes

print(fun(9))

