#Python  programme for printing Triangular Number Series
n = int(input('Enter how many triangular numbers you want to print : '))
m = 0
# for i in range(n):
#     m += i
#     print(f' {m} ',end="")
def traingle(i,n,m):
    if(i==n):
        return
    print(f' {m} ',end="")
    m += i
    traingle(i+1,n,m)

traingle(0,n,0)