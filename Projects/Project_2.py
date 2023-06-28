# Project_2   Guess Number  641 229
import random 
upper_bond = int(input("Enter the upper bond of guessing number :" ))
while True:
    if(upper_bond <= 0):
        upper_bond = int(input("Please enter a +ve number : " ))
    else:
        break
rand_num = random.randint(0,upper_bond)
guess = 0
count = 0
print(f'Guess the number between 0  and {upper_bond}')
while True:
    count +=1
    guess = int(input("Guess the number : "))
    if(guess==rand_num):
        print("Hoo you guess the number correctly!")
        break
    elif (guess > rand_num):
        print("You Guess Too High....")
    else:
        print("You Guess Too Low....")
print(f"You guess the number in {count} attempts")