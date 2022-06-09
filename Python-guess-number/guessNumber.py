import random

def guess(x):
    random_number = random.randint(1,x)
    print("Let's play a little guessing game")
    print("But First I need to know about you")
    player_name = input("Hello, What is your name? ")
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print("Sorry , guess again. That is too high.")
            
    print(f'Well Done {player_name}, You have guessed the right number {random_number} correctly!!')
    
guess(20);