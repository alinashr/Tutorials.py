#tut45_chap3_ex2.py

# Ask useer's nalinaame and age
# If user's name start with ('a' or 'A') and age is above 10 then
# print 'you can watch coco movie'
# else print 'sorry you cannot watch coco'

name,age= input("ENter name and age : ").split(",")
age=int(age)
if (name[0]=='a' or 'A')  and age >= 10:
    print(" You can watch coco movie ")
else:
    print(" You cannot watch coco movie ") 

nme=input("Enter your name")
ae=int(input("Enter your age"))
if nme=='ac' and ae==23:
    print("C")
else:
    print("Cj")
