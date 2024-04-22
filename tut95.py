#chap 5 ex-1

# define a function which will take list containing numbers as input and return list containing square of every elements


# example 
# numbers = [1,2,3,4]
# square_list(numbers)  ------>  [1,4,9,16]


# numbers = [1,2,3,4]
# def square_list(n):
#     square = []
#     for i in n:
#         square.append(i*i)
        
#     return square

# numbers=list(range(1,11))

# print(square_list(numbers))

num=list(range(1,7,2))   #for direct input of numbers
def sq_num(num):
    sq=[]
    for i in num:
        sq.append(i**2)
    return sq

print(sq_num(num))


# li=[1,23,4]
# li.extend([23,3])
# # li.append([23,3])

# print(li)


# l1=[1,2,3]
# l2=[4,5,6]
# l=l1+l2
# print(l)

# lidd=[1,2,4,5]
# print(lidd)
# print("After inserting 3 in the particular position(2nd)")
# lidd.insert(2,3)
# print(lidd)

#Removing from list
li=[1,2,3,4]
li.pop(0)
print(li)

















