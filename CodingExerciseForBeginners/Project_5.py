#Project_5
#Scilent Auction Program

import os
print("****Welcome to Scilent Auction Program****")
flag = True
auction_members = dict()
flag = True
while(flag):
    name = input("Enter your name : ")
    bid = int(input("What is your bid : "))
    auction_members[name] = bid
    repeat = input("Are there any bidders ? Type 'yes' or 'no' : ")
    if(repeat == 'yes'):
        os.system('cls')
    else:
        flag = False

max_key = max(auction_members, key=lambda k: auction_members[k])
print(f'The winner is {max_key} with a bid of {auction_members[max_key]}')


