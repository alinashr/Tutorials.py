# ask a user for name 
# E.g: Alina Shrestha 
# print count of each 
# output:
#      A - 1
#      l - 1 
#      i - 1
#      n - 1
#      a - 2
#        -1
#      S - 1
#      h - 2
#      r - 1
#      e - 1
#      s - 1
#      t - 1
 
# easy method    
# name=input("Enter your full name : ")
# print("A - ",name.count("A"))
# print("l - ",name.count("l"))
# print("i - ",name.count("i"))
# print("n - ",name.count("n"))
# print("a - ",name.count("a"))
# print("  - ",name.count(" "))
# print("S - ",name.count("S"))
# print("h - ",name.count("h"))
# print("r - ",name.count("r"))
# print("e - ",name.count("e"))
# print("s - ",name.count("s"))
# print("t - ",name.count("t"))


# Another method(quite complex)
name=input("Enter your full name : ")
temp_var=""
i=0
while i<len(name):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1  
