#Python programme to print the arthematic series
a = int(input('Enter intial value : '))
d = int(input('Enter the difference between numbers : '))
n = int(input('Enter how many numbers you want to print : '))
for i in range(n):
    print(f'{a}',end=" ")
    a += d