import random

number=random.randint(1, 100)
player_name = input("Hello, What's your name?")

print('ok! '+ player_name+ '  Guessing a number between 1 and 10:')

number_of_guesses = 0 

while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1

        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            break