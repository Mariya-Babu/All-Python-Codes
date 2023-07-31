#Python programme for printing X-pattern
n = int(input('Enter n value : '))
# for i in range(n):
#     for j in range(2*n):
#         if(i==j or j==2*n-i-2):
#             print('X',end="")
#         else:
#             print(' ',end="")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(2*n):
#         if(i==j or j==2*n-i-2):
#             print('X',end="")
#         else:
#             print(' ',end="")
#     print()

for i in range(n):
    for j in range(n):
        if(i==j or j==n-i-1):
            print('X',end="")
        else:
            print(' ',end="")
    print()