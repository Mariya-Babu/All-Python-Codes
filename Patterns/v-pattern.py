#Python programme to print V-pattern
n = int(input('Enter n value : '))
for i in range(n):
    for j in range(2*n-1):
        if(i==j or (2*n-1)==i+j+1):
            print('V',end="")
        else:
            print(' ',end="")
    print()