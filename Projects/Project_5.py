# Project_5
# Password Encription 
def view():
    with open('passwords.txt','r') as fo:
        for line in fo.readlines():
            data = line.rstrip()
            user_name , password = data.split('|')
            print('User Name : ',user_name,'|','Password : ',password)
def add():
    user_name = input("Enter User name : ")
    password = input('Enter Password : ')
    with  open('passwords.txt', 'a') as fo:
        fo.write(user_name + "|" + password + "\n")
psw = input('Enter the Master password : ')
opt = input('view password and add password (view/add) Q for quit : ').lower()
if opt == 'view':
    view()
elif opt == 'add':
    add()
else:
    print('Invalid Entry.....')