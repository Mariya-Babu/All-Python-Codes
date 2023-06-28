n = int(input("Enter the n value:"))
fact = 0
for i in range(1,n,1):
    fact = 0
    for j in range(1,i):
        if(i%j==0):
            fact += j
    if(fact == i):
        print(f"{i} is perfect number!")   

print("Programme is finished ")
print("Hello World")