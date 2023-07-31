# WAP to find the maximum number from a list P_45
l = input('Enter the list elements seperated by space : ')
print(f'{l} before split')
l = l.split()
print(f'{l} aftr split')
max_ele = -99999
for ele in l:
    if(int(ele) > max_ele):
        max_ele = int(ele)
print(f'The maximum element from the list = {max_ele}')