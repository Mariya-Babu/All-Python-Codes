total_saving = 0
mon_saving = 100
curr_saving = mon_saving
days = int(input("Enter no.of days : "))
for i in range(days):
    if(i%7<5):
        total_saving += curr_saving
        curr_saving += 100
    if(i%7==6):
        mon_saving += 100
        curr_saving = mon_saving
        # print(f"{i%7} = Current saing {curr_saving} \n ")
    # print(f"{i%7} = Current saing {curr_saving} \n ")

print(total_saving) 