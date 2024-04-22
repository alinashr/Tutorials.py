#Dictionary comprehension
 
# square={1:1,2:4,3:9,4:16}

sq={f"square of {i} is ":i*i for i in range(1,5)}
# print(sq)

#for loops in dictionary
for k,v in sq.items():
    print(f"{k}: {v}  ")


#dictionary comprehension that counts the no of letter in name

name="alsinaS"
dicr = {char:name.count(char) for char in name}
print(dicr)