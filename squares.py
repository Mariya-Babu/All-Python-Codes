import random
l = list()
for i in range(11,21):
    l.append(i)
print("[  ",end="")
for i in range(len(l)):
    print(l[i]," ",end=" ")
print(" ]")
for i in range(11,21):
    print(i," X ",i," = ",i*i)
x = 1
score = 100
count = 0
while(x):
    count = 0
    for i in range(10):
        for j in range(10):
            x = l[i]
            print(x," X ",x," = ",end=" ")
            y = int(input())
            if(y==x*x):
                continue
            else:
                print("Wrong")
                continue
            
    for i in range(50):
        x = random.choice(l)
        print(x," = ",end=" ")
        y = int(input())
        if(y==x*x):
            continue
        else:
            print("Wrong")
            count +=1
            continue
    print("Your score is : ",score - 2*count)
    x = int(input("If you want to exit enter 0  otherwise enter 1 : "))
