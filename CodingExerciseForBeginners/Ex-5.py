#Find out how many days, weeks months we have left if we live until 90 years old 
# 1year = 365 days 
# 1year = 52 weeks
# 1year = 12 months
age = int(input('Enter your age : '))
total_years = 90

remaining_years = total_years - age
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365

print(f'You have {remaining_days} days, {remaining_weeks} weeks, {remaining_months} months left')