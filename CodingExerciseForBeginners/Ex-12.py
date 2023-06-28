#WAP to select a random name from a list of names and the person select will  have to pay for everybody's food bill. P-35
import random
names = input('Enter your names seperated by space : ')
names = names.split()
print(names)
# rand_name = random.choice(names)
l = len(names)
rand_num = random.randint(0,l-1)
print(f'{names[rand_num]} will pay the bill')