# Ask a user name and print back username in reverse order


#NOte : try to make your program in 2 lines using string formatting

name=input("enter your name : ")
print(name[-1::-1])
# print(f "Your reverse order is " {name[::-1]})  error

print(f"Your reverse order is {name[::-1]}")

name=input("Enter your name")
print(f"THe name in reverse order is {name[-1::-1]}")
