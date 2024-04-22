#Ask a user to input 3 numbers and you have to print average of three  numbers using string formatting

num1,num2,num3=input("Enter three numbers: ").split(",")

num4=(int(num1)+int(num2)+int(num3))/3
print(num4)

print(f"THe average of threee numbers is {(int(num1)+int(num2)+int(num3))/3}")
print(f"THe average of threee numbers is {num4}")

