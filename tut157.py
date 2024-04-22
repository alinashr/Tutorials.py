


# l1 = [1,3,5,7]   #=> output to obtain
# l2 = [2,4,6,8]

# zip function part 2 

l = (1,2) , (3,4), (5,6), (7,8)

# # * opererator with zip   = list unpack

# l1,l2=(zip(*l))   #unzipping
# print(list(l1))
# # print(list(l2))

l1 = [1,3,8,9]   #=> output to obtain
l2 = [2,4,6,8]

new_list =[]    # [2,4,6,9]
for p in zip(l1 ,l2):
    new_list.append(min(p))

print(new_list)




