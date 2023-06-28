#Python Programme to print Odd Number Series 
n = int(input('Enter how many number of odd numbers you want to print : '))
for i in range(2*n):
    if(i%2 !=0):
        print(f'{i}',end=" ")
