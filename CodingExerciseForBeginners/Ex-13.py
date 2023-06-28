#Nested List Problem  P_38
final_list = [[1,1,1],[1,1,1],[1,1,1]]
print(final_list)
pos = input('Enter the position where you want to store the money : ')
row = int(pos[0])
col = int(pos[1])
final_list[row-1][col-1] = 'X'
print(final_list)