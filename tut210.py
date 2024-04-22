# Chapter 17 exercise 1
#make a function 'divide'
#divide(a,b)

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as er:
        # print('You cannot divide  by zero')
        print(er)
    except TypeError as err:
        print(err)
    except:
        print("Unexpected Error")

print(divide(8, ))

# print(divide(4,2))   #2
# print(divide(4,0))  #please don't divide by zero, Zero
# print(divide('4',2))  #please input numbers only















