
# looping in tuples
# tuple with one Element 
# tuple without parenthesis 
# tuple unpacking 
# list inside tuple 
# some functions that you can use with tuple


# val = (5)
# print(type(val))
# mixed = (1,2,3,4)
# print(type(mixed))
# len = len(mixed)
# print(len)
# i=0

# #loop
mixed=(1,2,3,4)
for i in  mixed:
    print(i)
while i<len(mixed):
    print(i)
    i=i+1



# # tuple with one Element
# one = ('ant',)
# val = (5)
# print(type(one))

# # tuple without parenthesis
# num = 1,2,3
# print(type(num))

# print("\n")
# # tuple unpacking  
# color = ('Red','Green','Blue')
# color1,color2,color3 = color 
# print(color1)
# print(color2)
# print(color3)

# inn = [4,5,6]
# inn.pop()
# print(inn)
# list inside tuple 
fruit = ([1,2,'3'],[4,5,6])
kf=(1)
kfi=(1,)
print(type(kf))
print(type(kfi))
fruit[0].pop()
fruit[1].pop()
print(fruit)
print(fruit[1]) 
print(type(fruit))

# # some functions that you can use with tuple
# #sum(),min(),max()

# mixed = (1,2,3,4)
# print(min(mixed))
# print(max(mixed))