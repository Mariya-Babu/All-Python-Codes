def check_year(year):
    if(year%4==0):
        if(year%100==0):
            # print('Given year is not a leap year!')
            return 0
            if(year%400==0):
                # print('Given year is leap year ')
                return 1
            else:
                # print('Given year is not a leap year ')
                return 0
        else:
            # print('Given year is a leap year ')
            return  
        # print('Given year is not a leap year ')
        return 0


year = int(input('Enter a year to check whether a given year is leap_year or not : '))
month = int(input('Enter the month number : '))

leap_year = check_year(year)

month_days = {
    1 : [31,'Jan'],
    2 : [28,'Feb'],
    3 : [31,'Mar'],
    4 : [30,'April'],
    5 : [31,'May'],
    6 : [30,'June'],
    7 : [31,'July'],
    8 : [31,'Aug'],
    9 : [30,'Sep'],
    10 : [31,'Oct'],
    11 : [30,'Nov'],
    12 : [31,'Dec'],

}

if(leap_year and month == 2):
    print('Feb having 29 days!')
else:
    print(f'{month_days[month][1]} having {month_days[month][0]}!')