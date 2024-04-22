#min and max function

num = [1,2,3,5]
print(type(num))
print("HEllo world I am learning python")
print(min(num))
print(max(num))

#take a list as input in function and output the difference of highest and lowest 

def diff_num(n):
    mi=min(n)
    ma=max(n)
    return ma-mi

print("The diff of the highest and the lowest is : ")
print(diff_num(num))