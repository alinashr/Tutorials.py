#Advance Function Practice 1 

# import numbers


# Define a function take any no. of lists containing numbers
# [1,2,3] , [4,5,6] , [7,8,9]
# return average
# # (1+4+7)/3 , (2,5,8)/3 , (3,6,9)/3

# def avg(l1,l2):
#     average=[]
#     for pair in zip(l1,l2):
#         average.append(sum(pair)/len(pair))
#     return average
# print(avg([2,3,4],[2,6,4]))

# def avg_finder(l1,l2):
#     average=[]
#     for pair in zip(l1,l2):
#         average.append(sum(pair)/len(pair))
#     return average
# print(avg_finder([1,2,4],[5,6,7]))

# for multiple lists
# def avg_finder(*args):
#     average=[]
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average
# print(avg_finder([1,2,4],[5,6,7],[3,1,1]))

# try to make the function anonymous using one line with lambda 

# using lambda and list comprehension

# average_finder = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)] 
# print(average_finder([1,2,4],[5,6,7],[3,1,1]))

average_finder = lambda l1,l2:[sum(pair)/len(pair) for pair in zip(l1,l2)] 
print(average_finder([1,2,4],[5,6,7]))

