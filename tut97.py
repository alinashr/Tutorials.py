# #chap 5 - ex 2

# #define a function which will take as a argument and this functio will return a reversed list

# # examples
# # [1,2,3,4] ----> [4,3,2,1]

# # ['word1','word2'] ---> ['word2','word1']

# # Note you simply do this with the reverse method or [::-1]
# # But try to do thid with the help of append and return method


# # def func_arg(argg):
#     # return argg[::-1]


# # def func_arg(argg):
# #     return argg[::-1]

# # string = ['word1','word2','word3']
# # print(func_arg(string))

# #    reverse=[]
# #     for i in argg:
# #         i.reverse(argg)
# #         i=i+1
# #     return reverse

# # def reverse_list(l):
# #     r_list = []
# #     for i in range(0,len(l)):
# #         popped_item = l.pop()
# #         r_list.append(popped_item)
# #     return r_list
# # numbers = [1,2,3,4]
# # print(reverse_list(numbers))

def pop_re(l):
    pp = []
    for i in range(len(l)):
        popped_item = l.pop()
        pp.append(popped_item)
    return pp
numbers = [1,8,3,4]
print(pop_re(numbers))


# n=[1,2,3,4]
# def rec(n):
#     rev=[]
#     for i in n:
#         poppp=n.pop()
#         rev.append(poppp)
#     return rev
# print(rec(n))

# n=[1,2,3,4]
# def rec(n):
#     rev=[]
#     for i in n:
#         rev.append(n[::-1])
#         return rev
# print(rec(n))



# 1) Reverse method
# n=[1,2,3,4]
# def rec(n):
#     n.reverse()
#     return n
# print(rec(n))

# 2) String Slicing
# n=[1,2,3,4]
# def rec(n):
#     print(n[::-1])
    

# (rec(n))

# 3) Append and Pop Method

# n=[1,2,3,4]
# def rec(n):
#     rev=[]
#     for i in n:
#         rev.append(n[::-1])
#         return rev
# print(rec(n))















