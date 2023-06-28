#Love Calculate P_31
name1 = input('Enter your Name1 : ').lower()
name2 = input('Enter your  Name2 : ').lower()
full_name = name1+name2
t = 'true'
true = 0
l = 'love'
love = 0
for letter in t:
    true += full_name.count(letter)
for letter in l:
    love +=full_name.count(letter)

score = str(true) + str(love)
truelove = true + love

if(truelove < 10 or truelove > 90):
    print(f'Your score is {score} you both are like fish and fisherman ')
elif(truelove >=40 and truelove <=50):
    print(f'Your score is {score} and you both are made for each other!')
else:
    print(f'Your score is {score}')