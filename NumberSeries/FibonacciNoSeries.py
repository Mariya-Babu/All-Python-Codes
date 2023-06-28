#Python programme to print fibonacci series
n = int(input('Enter n value : '))
a = 0
b = 1
for i in range(n):
    c = a + b
    a = b
    b = c
    print(f'{c}',end=" ")