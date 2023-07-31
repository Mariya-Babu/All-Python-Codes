#Python programme for printing Y-pattern
n = int(input('Enter n value : '))
for i in range(n):
    for j in range(2*n):
        if(i==j or j==2*n-i-2):
            print('Y',end="")
        else:
            print(' ',end="")
    print()
for i in range(n//2):
    for j in range(n-1):
        print(' ',end="")
    print('Y')