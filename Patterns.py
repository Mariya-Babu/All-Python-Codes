n = int(input('Enter n value : '))
m = 2 * n - 1
k = 0
for i in range(n):
    for j in range(k):
        print(' ',end="")
    for j in range(m - 2*k):
        print('x',end='')
    for j in range(k):
        print(' ',end='')
    k += 1
    print()