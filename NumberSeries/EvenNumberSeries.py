#Python Programme to print Even Number Series
n = int(input('Enter how many no.of even number you want to print : '))
for i in range(n*2):
    # print(f'{i%2==0}',end=" ")
    if(i%2==0):
        print(f'{i}',end=" ")