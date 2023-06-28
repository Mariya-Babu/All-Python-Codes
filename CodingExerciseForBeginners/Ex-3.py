# Programme to add digit's of the given input number 

num = int(input('Enter a number to add the digit\'s  of the number : '))
print(f'num = {num}')

temp = num
res = 0
while(temp != 0):
    res += temp % 10
    temp = temp//10

print(f'sum of the digits of {num} = {res}')