# This shows the challenge for match case

import random

guess = int(input("Guess a number: "))

secret_number = random.randint(1,20)

match guess:
    case guess if guess > secret_number:
        print("Your guess is too high")
    case guess if guess < secret_number:
        print("your guess is kind of low")
    case guess if guess == secret_number:
        print("Congratulations, You guessed it")

