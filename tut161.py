# any and all function practice

def sum_num(*args):
    if all([type(arg)==int or type(arg)==float for arg in args]):
        # pri=([type(arg) for arg in args])
        # print(pri)
        total=0
        for arg in args:
            total=total+arg
        return total
    else: 
        return "Wrong input"

print(sum_num(1,2,3,4,5,9,1))    