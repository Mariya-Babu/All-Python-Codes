# Project_7
# Computer Guess
import random

def computer_guess(x):
    low = 1
    high = x
    rand_num = random.randint(1,x)
    user_input = int(input("Enter your number to guess : "))
    guess = 0
    while guess != user_input :
        if (low != high):
            guess = random.randint(low,high)
        else:
            guess = low
        print(f"Computer guess is {guess} ")
        ch = input("Enter (H) for High and (L) for  Low and (C) Correct ").lower()
        if ch=='h':
            high = guess - 1
        elif ch == 'l':
            low = guess + 1
        elif ch =='c':
            print(f"Hoo Computer guess the number correctly! that is {guess}")
            break
        else:
            print('Invalid Input')
    print("Game Over!")

computer_guess(1000)