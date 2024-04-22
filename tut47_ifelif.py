num=int(input("Enter any number"))


if num==0:
    print("It cannot divide any even number ")

elif num%2==0:
    print("It can divide any positive even number")
elif num%2!=0:
    print("It cannot divide any positive integer")

else:
    print("You have entered negetive integer") 

ans=88/num
ans=int(ans)
print(ans)    