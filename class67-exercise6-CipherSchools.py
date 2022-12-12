   # guessing the number
# ask until it is right
# if it is equal then print you won after n attempts
import random
lucky_number = random.randint(1,101)
no_of_guesses = 0
guess_limit = 10
while no_of_guesses < guess_limit:
    guess =int(input("guess the number: "))
    no_of_guesses += 1
    if guess < lucky_number:
        print("too low")
    elif guess>lucky_number:
        print("too high")
    elif guess==lucky_number:
        print(f"congratulations you won after {no_of_guesses} attempts")
        break

# sir method
winning_number = random.randint(1,100)
guess = 1
number = int(input("guess a number between 1 and 100: "))
game_over = False
while not game_over:
    if number == winning_number:
        print(f"you win, and you guessed this number in {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print('too low')
            guess += 1
            number = int(input('guess the number again: '))
        else:
            print('too high')
            guess += 1
            number = int(input('guess the number again: '))