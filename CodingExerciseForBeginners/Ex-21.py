# Calculating the no.of paint can's needed to paint a wall
import math
#Function to calculate cans required to paint a wall
def cansRequired(height,width,coverage):
    area = height * width
    cansNeeded = area / coverage
    cansNeeded = math.ceil(cansNeeded)
    return cansNeeded


height = int(input("Enter the height of the wall : "))
width = int(input("Enter the width of the wall : "))
coverage = int(input("Enter how much area one cane can cover : "))
print(f"Cans Need to paint the wall = {cansRequired(height,width,coverage)}")
 