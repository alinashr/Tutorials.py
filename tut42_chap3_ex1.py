# # "Chapter 3 Exercise1"
# # Make a variable, like winning number and assign any number to it
# # Ask user to guess a number IF user guessed correctly then print "YOU WON!!!"
# # if user didn't guessed correctly then:
# #     if user guessed lower than actual number then porint "too low"
# #     if user guessed higher than actual number then print "too high"

# # google "how to generate random number in python " to generate random 
# # winning number

# winning_num=45
# guess=input("Enter number: ")
# guess=int(guess)
# if guess == winning_num:
#     print("You won")
# else:
#     if guess < winning_num:
#         print("Too low")
#     else: 
#         print("Too high")

# '''
# guess=input("Enter number: ")
# import random
# no = random.randint(1,10)
# while True:
#    guess = input("Guess:")
#    if int(guess) == no:
#       print("YOU WON");
#       break
#    else:
#       print("TRY AGAIN")
# '''

Number = 7
while True:
    guess = int(input("Guess a number between 1 and 10 > "))
    if guess == Number:
        print("You Guessed Correct Number. Congratulations!!")
        break;
    else:  
        print("Wrong Number. Try Again!! ")





# import random


# class GuessingGame:
#     def __init__(self, low=0, high=100):
#         self.low = low
#         self.high = high

#     def is_guess_within_range(self, guess):
#         '''Check if the guess is within the range of self.low and self.high'''

#         return self.low <= guess <= self.high

#     def get_user_guess(self):
#         '''Ask user to enter their guess until the valid guess is entered.'''

#         guess = None

#         while not guess:
#             try:
#                 guess = int(input(f'\nGuess a number between {self.low}-{self.high}: '))

#                 if not self.is_guess_within_range(guess):
#                     print(f'Your guess must be in {self.low}-{self.high}')
#                     guess = None

#             except ValueError:
#                 print('Your guess is not valid. Guess was expected in integer')

#         return guess

#     def play_again(self):
#         '''Ask user if they want to play the game again.'''

#         check = input('\nDo you want to play again (y/n)?').lower()

#         return check == 'y'

#     def random_number(self):
#         '''Returns random number which has to be guessed by the user'''

#         return random.randint(self.low, self.high)

#     def main(self):
#         '''Playing the game'''

#         play = True

#         while play:
#             count = 1
#             is_guessed = False
#             to_guess = self.random_number()

#             while not is_guessed:   # Until user guesses the random_number
#                 user_guess = self.get_user_guess()

#                 if user_guess == to_guess:
#                     is_guessed = True
#                     print(f'You have guessed in {count} guesses')

#                     if not self.play_again():
#                         play = False

#                 elif user_guess > to_guess:
#                     print('Your guess is high')

#                 elif user_guess < to_guess:
#                     print('Your guess is low')

#                 count += 1


# if __name__ == '__main__':
#     guess = GuessingGame()
#     guess.main()

# '''
