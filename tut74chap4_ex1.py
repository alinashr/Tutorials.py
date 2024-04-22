# python tut74chap4_ex1.py

# define a fucntion which takes two numbers as a input and return the greater of two 

def larger(a,b):
    if a > b:
        return a
    return b

num1=int(input("ENTER THE num1  : "))
num2=int(input("ENTER THE num2 : "))

print(larger(num1,num2))

