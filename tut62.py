# from http.server import SimpleHTTPRequestHandler


# practice for loop
# ask user name and count each character 
# Alina Shrestha 

# A : 1
# l : 1
# i : 1
# n : 1
# a : 2
#   : 1
# S : 1
# h : 2
# r : 1
# e : 1
# s : 1
# t : 1

name= input("Enter your full name : ")
temp=""

for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]