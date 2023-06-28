# Project_3 Rock/Paper/Scissor
import random
option = ['rock','paper','scissor']
user_score = 0
computer_score = 0
while True:
    user_choice = input("rock/paper/scissor Q for quite : ").lower()
    if user_choice == 'q' or user_choice == 'quite':
        break
    elif user_choice not in option:
        print("You Entered wrong info please enter correct into ")
        continue
    rand_num = random.randint(0,2)
    computer_choice = option[rand_num]
    print(computer_choice)
    if (user_choice=='rock' and computer_choice == 'scissor'):
        print("You Win!")
        user_score += 1
        continue
    elif (user_choice == 'paper' and computer_choice  == 'rock'):
        print("You Win!")
        user_score +=1
        continue
    elif (user_choice == 'scissor' and computer_choice == 'paper'):
        print('You Win!')
        user_score += 1
    elif (user_choice == computer_choice):
        print("Oops! Both Choose the same objcet....")
        continue
    else:
        print("Computer Win!")
        computer_score += 1
        continue
print("Game Over!")
print(f"You got {user_score} pointes and computer got {computer_score} points")


