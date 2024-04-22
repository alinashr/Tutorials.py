# guessing number modification
# import random
winning_num = 43
guess = 1  # counts the no of guesses
num = int(input("Guess a number between 1 to 100 :"))
game_over = False

while not game_over:
    if num == winning_num:
        print(f"you win and you guesses this number in {guess} times")
        game_over = True

    else:
        if num < winning_num:
            print("Too low")
            guess += 1
            num=int(input("Guess again : "))
        else:
            print("Too high")
            guess += 1
            num=int(input("Guess again : "))
            