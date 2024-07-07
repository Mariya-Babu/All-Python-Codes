# Project - 8
# High or Low 
import random
import os

import DataBase as db 
import HigherLowerLogo as hll
import VS_Logo 

vs = VS_Logo.vs
higher_lower_log = hll.higher_lower

data = db.data
unvisited_data = list(data)
visited_data = []

c1 = random.choice(unvisited_data)
visited_data.append(c1)
unvisited_data.remove(c1)

c2 = random.choice(unvisited_data)
unvisited_data.remove(c2)
visited_data.append(c2)

score = 0
print(higher_lower_log)
print("Higher or Lower Game ")
flag = True
while flag:
    if unvisited_data:
        print(f'Compare 1 : {c1["name"]}, {c1["description"]}, {c1["country"]}')
        print(vs)
        print(f"Compare 2: {c2['name']}, {c2['description']}, {c2['country']}")
        answer = int(input("Who has more followers? '1' or '2' : "))

        if answer==1 and c1['follower_count'] >= c2['follower_count'] :
            c2 = random.choice(unvisited_data)
            unvisited_data.remove(c2)
            visited_data.append(c2)
        elif answer == 2 and c2['follower_count'] >= c1['follower_count'] :
            c1 = c2
            c2 = random.choice(unvisited_data)
            unvisited_data.remove(c2)
            visited_data.append(c2)
            score += 1
            print(higher_lower_log)
            print(f'Your are right. Your score is {score}')
        else: 
            os.system('cls')
            print(higher_lower_log)
            print(f'Your are Wrong. Your score is {score}')
            flag = False
            break
        os.system('cls')
        print(higher_lower_log)
        score += 1
        print(f'Your are right. Your score is {score}')
    else:
        print(f"You have own the Game. Your score {score}")
        flag = False
    
print(f"Your Game is Completed!. Your score is {score}")

