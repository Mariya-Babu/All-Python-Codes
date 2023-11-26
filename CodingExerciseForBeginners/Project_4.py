# Project - 4
# Caesar Cipher 

# Begining of Encryption fn to encrypt the given message
def Encryption(msg, key):
    Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    N = 26
    str = ''
    print("Encryption!....")
    for letter in msg:
        if letter.isalpha():
            x = (Alphabets.index(letter) + key ) % N
            if x < 0 :
                x += 26
            str = f'{str}{Alphabets[x]}'
        else:
            str =  f'{str}{letter}'
    
    print(f'The Encrypted message is : {str}')

# Begining of Encryption fn to encrypt the given message
def Decryption(msg, key):
    Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    N = 26
    str = ''
    print("Decryption!....")
    for letter in msg:
        if letter.isalpha():
            x = (Alphabets.index(letter) - key ) % N
            if x < 0 :
                x += 26
            str = f'{str}{Alphabets[x]}'
        else:
            str =  f'{str}{letter}'
    
    print(f'The Decrypted message is : {str}')
   
# Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print("Welcome to Caesar Cipher Web App You can Encrypt/Decrypt your messages using this App ")
flag = True
while(flag):
    print("Type 'encrypt' for encryption, type 'decrypt' for decryption : ")
    choice = input()
    print("Type your message : ")
    msg = input()
    print("Type the shift number : ")
    key = int(input())

    print(f' your choice is {choice}')

    # Comparing User Choice 
    if (choice == 'encrypt'):
        Encryption(msg,key)
    elif (choice == 'decrypt'):
        Decryption(msg,key)
    else:
        print('Invalid entry please Enter again ')


    repeat = input("Enter yes if you want to repeat otherwise enter  no :")
    
    if (repeat == 'no'):
        print(f'Your entered {choice} so you don\'t want to repeat this right  ')
    else:
        print(f'you entered {choice} so you want to repeat this right ')
    if (repeat == 'no'):
        flag = False
print("Programme completed successfully...")

