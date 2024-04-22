# Returning Function By Function

# def outer_func():
#     def inner_func():
#         print('inside inner func')
#     return inner_func

# v=outer_func()
# print(outer_func())   #prints -> <function outer_func.<locals>.inner_func at 0x00000152EA698EA0>
# v()    #prints -> inside inner func

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2
var=outer_func2("hello alina")
var()

