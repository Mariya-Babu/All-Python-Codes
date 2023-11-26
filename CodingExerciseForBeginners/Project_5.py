#Project_5
#Scilent Auction Program

def cls():
    pass
print("****Welcome to Scilent Auction Program****")
flag = True
auction_members = dict()
flag = True
while(flag):
    name = input("Enter your name : ")
    bid = int(input("What is your bid : "))
    auction_members[name] = bid
    repeat = input("Are there any bidders ? Type 'yes' or 'no' ")
    if(repeat == 'yes'):
        cls()
    else:
        flag = False

print(f'The winner is ')


