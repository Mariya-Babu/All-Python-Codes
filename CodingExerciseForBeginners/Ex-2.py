# Swapint of two numbers 

a = int(input('Enter value for a : '))
b = int(input('Enter value for b : '))

print(f'Before Swaping the a and b a = {a} b = {b}')
c = a + b
a = c - a
b = c - a

print(f'After Swaping the a and b a = {a} b = {b}')
