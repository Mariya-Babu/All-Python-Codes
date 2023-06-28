a = input("Enter the number to add the digit's of the number's : ")
sum = 0
for i in range(len(a)):
    sum += int(a[i])
print("The sum of the digit's of the number is : ",sum)
