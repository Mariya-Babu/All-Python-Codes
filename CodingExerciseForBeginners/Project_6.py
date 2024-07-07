#Project_5
#Python project to create a  calculator

import os

def calculate(num1,num2,operation):
    result = 0

    #calculataing the result 
    if (operation == '+'):
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*' :
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print('Invalid Entry ')
        return False

    print(f'{num1} {operation} {num2} = {result}')
    repeat = input(f"Enter 'y' to continue with {result} or 'n' to start new calculation 'x' to exit : ")

    if repeat == 'y':
        num1 = result
        num2 = int(input("Enter second number : "))
        operation = input("pick an operation : ")
        calculate(num1,num2,operation)
    elif repeat == 'n':
        os.system('cls')
        return True
    elif repeat == 'x':
        return False
    else:
        print('Invalid Entry...')
    
    return False


# Main Function 
print("Welcome to the Simple Calculator App ")
flag = True
while(flag):
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation : ")
    flag = calculate(num1,num2,operation)

print("Code Execution Completed!")