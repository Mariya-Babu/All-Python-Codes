# Coding Exercise for Calculating BMI

weight = int(input('Enter your Weight in kgs : '))
height = float(input('Enter your weight in centimeters : '))

height = height/100

BMI = weight/(height*height)
print(f'Your BMI is = {BMI}')
