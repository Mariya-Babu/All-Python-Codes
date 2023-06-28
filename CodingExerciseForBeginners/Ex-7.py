# Calculating BMI and telling which catageory he is 
import math
weight = int(input('Enter your weight in Kg : '))
height = int(input('Enter your height in cm : '))

height = height/100
bmi = weight/(height ** 2)

print(f'Your weight in kgs = {weight}')
print(f'Your weight in meters = {height}')
print(f'Yoru BMI = {bmi}')
min_weigth = 18.5 * (height ** 2)
max_weight =  24.9 * (height ** 2)

if(bmi<16.0):
    print(f'Severe thinness')
    print(f'Gain {min_weigth - weight} to maintain the noraml range of Bmi... ')
elif (bmi>16.0 and bmi<16.9):
    print(f'Moderate thinness ')
    print(f'Gain {min_weigth - weight} to maintain the noraml range of Bmi...')
elif (bmi>17.0 and bmi<18.4):
    print(f'Mild thinness')
    print(f'Gain {min_weigth - weight} to maintain the noraml range of Bmi...')
elif (bmi>18.5 and bmi<24.9):
    print(f'Normal range')
    print('Good Maintain the this range you will be healthy....')
elif(bmi>25.0 and bmi<29.9):
    print(f'Pre-obese')
    print(f'Loss {max_weight - weight} got maintain the noraml range of Bmi...')
elif(bmi>30.0 and bmi<34.9):
    print(f'Obese (Class I)')
    print(f'Loss {max_weight - weight} got maintain the noraml range of Bmi...')
elif(bmi>35.0 and bmi<39.9):
    print(f'Obese (Class II)')
    print(f'Loss {max_weight - weight} got maintain the noraml range of Bmi...')
else:
    print(f'Obese (Class III)')
    print(f'Loss {max_weight - weight} got maintain the noraml range of Bmi...')