path = input('Enter the file path : ')
file_name = input('Enter the file name : ')
ext = input('Enter the file extension : ')
try:
    with open(f'{path}/{file_name}.{ext}','x') as fo:
        print('File Created Successfully!')

except:
    print('File already exist!')
    bol = input('Do you want to replace it if yes enter y  if no enter n (y/n) : ')

    if(bol.lower() == 'y'):
        with open(f'{path}/{file_name}.{ext}','w') as fo:
            print('File replaced Successfully!')
    elif(bol.lower() == 'n'):
        print('Ok!')
    else:
        print("You enterd a wrong syntax")

finally:
    print('Programme Completed Successfully!')