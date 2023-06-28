#WAP to calculate the sum of the all even numbers between (0-100) 100 included using for loop and range 
sum = 0
for even_number in range(0,101,2):
    sum += even_number
print(f'The sum of all the even number in the range (0-101) is = {sum}')