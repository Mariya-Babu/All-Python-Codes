#programme to implement the squeroot of a given number
#Function to implement the squreroot of the number
def SqureRoot(n,dec):
    x = n
    i = 0
    root = 1
    while(i<dec):
        root = 0.5 * (x+(n/x))
        x = root
        i +=1
    return root
#Main Function
n = int(input("Enter a number to find the squeroot of the number :"))
dec = int(input("Enter how many digit you want to perform after the decimal :"))
result = SqureRoot(n,dec)
print(f"The squreroot of the given number is {result}")
