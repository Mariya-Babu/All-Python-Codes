import random
a = int(input('Enter n value : '))
score = 0
for i in range(1,11):
    print(f'{a} x {i} = {a*i}')

print()
for i in range(1,11):
    print(f'{a} x {i} = ',end=" ")
    x = int(input())
    if x == a*i:
        continue
    else:
        print('Wrong!')
for i in range(1,111):
    x = random.randrange(10)
    print(i,") ",a," x ",x," = ",end=" ")
    y = int(input())
    if(a*x==y):
        score += 1
        continue
    else:
        print("Wrong!")
print(f'your score is = {score}')
with open('C:\\Users\\RISHI\\Desktop\\PyCodes\\score.txt','a') as fo:
    fo.write(f'\n score = {score}')
