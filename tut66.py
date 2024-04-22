# guessing number modification
# import random
'''
# dry run of code 
# 1)
winning_num = 9
guess = 1  # counts the no of guesses
num = int(input("Guess a number between 1 to 10 :"))
# game_over = False

while True:
    if guess==3:
        print("Game over! sorry")
        break
    if num == winning_num:
        print(f"you win and you guesses this number in {guess} times")
        break

    else:
        if num < winning_num:
            print("wrong guess!")

        else:
            print("wrong guess!")

        guess += 1
        num=int(input("Guess again : "))    
'''
#using random module
import random
winning_num = random.randint(1,5)
guess = 1  # counts the no of guesses
num = int(input("Guess a number between 1 to 10 :"))
# game_over = False

while True:
    if guess==4:
        print("Game over! sorry")
        break
    if num == winning_num:
        print(f"you win and you guesses this number in {guess} times")
        break

    else:
        if num < winning_num:
            print("Too low")

        else:
            print("Too high")

        guess += 1
        num=int(input("Guess again : "))     


            
            