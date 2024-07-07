# Project_7
# Guess the number  (Human Guess)
import random
import GuessTheNumberAsciiArt as ascii_art

print(ascii_art.ascii_art)
print("Guess the Number Game ")
print("Let me think of a number between 1 to 50 ")
level = input("Choose level of difiiculty...Type 'easy' or 'hard' : ")
attempts = 0

computer_guess = random.randint(1,50)
human_guess = -1
if (level=='easy'):
    attempts = 10
elif (level == 'hard'):
    attempts = 5
else:
    print("Invalid Entry ")
    attempts = 0
while ((not computer_guess == human_guess) and (attempts > 0)):
    print(f"You have {attempts} attempts remaining to guess the number!")
    human_guess = int(input("Make a guess : "))
    
    if (human_guess < computer_guess ):
        print("Your Guess is Too Low ")
    elif (human_guess > computer_guess):
        print("Your Guess is Too High ")
    elif (human_guess == computer_guess):
        print(f"Your guess is right ... The answer was {human_guess}")
        break
    else:
        print("Invalid Entry")
        break
    print("Guess Again ")   
    attempts -= 1

if(attempts == 0):
    print(f"You Attempt's are completed! The answer was {computer_guess}")