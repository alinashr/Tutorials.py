# zip function
user_id=['user1','user2','user3','jhjh']
names=['Alina','sldfi','dfdf']
caste=['shrestha','dfdf','xxxx']
#('user1','alina'),('user2','sldfi')

print(list(zip(user_id,names,caste)))
# print(dict(zip(user_id,names)))
l=[('user1', 'Alina', 'shrestha'), ('user2', 'sldfi', 'dfdf'), ('user3', 'dfdf', 'xxxx')]
l1,l2,l3=list(zip(*l)) 
print(l1)
print(l2)
print(l3)




