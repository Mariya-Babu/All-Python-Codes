list = ['r','g','u','k','t']
n = len(list)
for i in range(n):
    for j in range(i+1):
        print(list[j],end="")
    print()

for i in range(n-1):
    for j in range(n-i-1):
        print(list[j],end="")
    print()