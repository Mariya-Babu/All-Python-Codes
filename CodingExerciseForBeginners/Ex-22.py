# Python Program to check the given number is prime or not
def primeNumberChecking(n):
    count = 0
    for i in range(2,n):
        if (n%i == 0):
            count += 1
    return count


print("Programme to check whether the given number is prime or not ")
n = int(input("Enter a number to check the number is prime or not : "))

if(primeNumberChecking(n) == 0):
    print("The given number is prime Number ")
else:
    print("The given number is not a prime number ")