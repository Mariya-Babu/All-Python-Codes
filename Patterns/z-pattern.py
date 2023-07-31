#Python programme for printing Z-pattern

n = int(input('Enter n value : '))

for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1):
            print('Z',end="  ")
        else:
            if(j==n-i-1):
                print('Z',end="  ")
            else:
                print(' ',end="  ")
    print()