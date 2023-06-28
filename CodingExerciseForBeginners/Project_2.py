#Random Password Generator
import random

print('Welcome to the password Generator!')
a = int(input('How many alphabet do want : '))     #Alphabet's count 
s = int(input('How many symbols would you like : '))    #special Characters length
num = int(input('How many numbers would you like : '))  #numbers 

n = a + s + num
rand_num = ''
rand_sym = ''
rand_alph = ''

#Random Alphabet's Generation 
for i in range(a):
    u = random.randint(65,90)
    l = random.randint(97,122)

    b = random.randint(0,1)
    if(b==0):
        rand_alph += chr(l)
    else:
        rand_alph += chr(u)

#Random Symbol's  Generation
l = ['','','','']
for i in range(s):
    # rand_ch = random.randrange(60,126)
    l[0] = random.randint(33,47)
    l[1] = random.randint(58,64)
    l[2] = random.randint(91,96)
    l[3] = random.randint(123,126)

    x = random.randint(0,3)

    rand_sym += chr(l[x])

#Random Numbers's Generation 
for i in range(num):
    rn = random.randint(48,57)
    rand_num += str(chr(rn))

print(f'Random Alphabet\'s = {rand_alph} Random Symbol\'s = {rand_sym} Random Number = {rand_num} ')
password =  rand_alph + rand_sym + rand_num
# rand_pass = ""

print(f'The Random Password without shuffling = {password}')

password = list(password)
print(f'The character of the password = {password}')
for i in range(n):
    x = random.randint(0,n-1)
    ch = password[i]
    password[i] = password[x]
    password[x] = ch

print(f'The character of the password after suffling = {password}')

rand_pass = ''
for i in range(n):
    rand_pass += password[i]
print(f'Random Password after suffle = {rand_pass}')