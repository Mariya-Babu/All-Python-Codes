#Python random module programme on Heads/Tails P-35
import random 
rand_num = random.randint(0,1)
if(rand_num == 0):
    rand_num = 't'
else:
    rand_num = 'h'
print(f'Gusses the Tosses coin is Head/Tails ')
user_input = input('H for Heads and T for Tails : ').lower()
if(user_input == rand_num):
    if(rand_num == 't'):
        print(f'Hey you gussed right it is tails')
    else:
        print(f'Hey you gussed right it is Heads')
else:
    if(rand_num == 't'):
        print(f'Hoo you  gussed wrong it is tails')
    else:
        print(f'Hoo you gussed wrong it is Heads')