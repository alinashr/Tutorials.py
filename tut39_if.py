# age=input("Enter your age")
# age=int(age)
# print((age))

# # if age >= 20:
# #     print("You are allowed to marry legally")

# # else:
# #     print("you are under age")  

# if  age > 18:
#     pass
# else:
#     print("you cannot vote")     


# print(i)

# building a guessing game
secret_word=56
guess=""
guess_count=0
guess_limit=3
out_of_guesses= False


while guess != secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        
        guess=input("Enter your guess : ")
        guess_count+=1
    else:
        out_of_guesses=True
        
if out_of_guesses:
    print("Out of guesses, you loss")
    
else:
    print("You won")
        






# i=9
# i=i+8
   




# i=5
# while i>=1:
#     print(i)
#     i-=1
# print(" k")



# words={
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four",
#     "5":"Five",
#     "6":"Six",
#     "7":"Seven",
# }
# print(words.get("p","not a valid key"))
# print(words["1"])

# num=False

# if num:
#     print("hello")
# else:
