#Leap Year Checker
#Problem: Determine if a year is a leap year

year = 2025

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = True
else:
    leap_year = False

print("Is leap year:", leap_year)
