#Wap to calculate the average height of the student using for loop P_44

#Function to calculate the length of the list
def length(heights):
    l = 0
    for height  in heights:
        l += 1
    return l

#Function to calculate the sum of the list
def Sum(heights,l):
    sum = 0
    for i in range(l):
        sum += int(heights[i])
    return sum

heights = input('Enter heights with seperated by space : ')
heights = heights.split()

l = length(heights)
sum = Sum(heights,l)
print(f'Total no.of person\'s are {l}')
avg_height = sum//l
print(f'The avg height of the person\'s = {avg_height}')