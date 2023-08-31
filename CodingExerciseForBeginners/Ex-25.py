#Checking the given year is Leap Year or Not
def check_year(year):
    #If a year is divided by 400 then it is a leap year 
    if(year%400 == 0):
        return True
    else:
        #If a year is divided by 100 and not divided by 100 then it is a leap year
        if(year%4==0 and year%100 !=0):
            return True
        else:
            return False


year = int(input('Enter a year to check whether a given year is leap_year or not : '))
month = int(input('Enter the month number : '))

isLeapYear = check_year(year)

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

if(isLeapYear and month == 2):
    print('Feb having 29 days!')
else:
    print(f'{month_days[month][1]} having {month_days[month][0]}!')