#chap 5 ex - 3


# define a function that take list of words as argument and 
# return list with reverse of every element in that list

# Example
# ['abc','tuv','ffa']  ---> ['cba','vut','aff']

# def revstr(s):
#     rev=[]
#     for i in s:
#         rev.append(i[::-1])
        
#     return rev

# words = ['Alina','Alisa','Harry']
# print(revstr(words))   



# def revstr(s):
#     rev=[]
#     for i in range(0,len(s)):
#         rev.append(s[i][::-1])
        
#     return rev

# fruits = ['apple','orange','grapes','mango']
# print(revstr(fruits))   




# define a function that take list of words as argument and 
# return list with reverse of every element in that list

# Example
# ['abc','tuv','ffa']  ---> ['cba','vut','aff']


words=['alina','alisa','aliza','angila']
def return_reverse(words):
    lst=[]
    for i in words:
        lst.append(i[::-1])
    return lst

print(return_reverse(words))


