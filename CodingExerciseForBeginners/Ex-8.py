# Write a Programme to check whether given year is leap year of Not  p_28
year = int(input('Enter a year to check whether a given year is leap_year or not : '))

if(year%4==0):
    if(year%100==0):
        print('Given year is not a leap year!')
        if(year%400==0):
            print('Given year is leap year ')
        else:
            print('Given year is not a leap year ')
    else:
        print('Given year is a leap year ')
else:
    print('Given year is not a leap year ')