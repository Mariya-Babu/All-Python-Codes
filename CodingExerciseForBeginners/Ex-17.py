#FizzByzz Job Interview Question P_48
for i in range(0,101):
    if(i%3==0 and i%5==0):
        print('FizzByzz')
    elif(i%3==0):
        print('Fizz')
    elif(i%5==0):
        print('Byzz')
    else:
        print(f'{i}')