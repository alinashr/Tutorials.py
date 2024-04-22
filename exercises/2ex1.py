#Ask a user to input 3 numbers and you have to print average of three  numbers using string formatting

n1,n2,n3=(input("Enter three numbers ").split(","))
average=(f"The average of three numbers is {int(n1+n2+n3)/3}")
print(average)