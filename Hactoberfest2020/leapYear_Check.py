year = input("Type the year which you want to check...\n")

def checkLeapYear(year):
    leapYear = False
    Year = int(year)
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                leapYear = True
            elif Year % 400 != 0:
                leapYear = False
            
        elif Year % 100 != 0:
            leapYear = True
    elif Year % 400 == 0:
        leapYear = True

    return leapYear

isLeapYear = checkLeapYear(year)
print(isLeapYear)
if isLeapYear == True:
    print(f"yes {year} is a leap Year.")
else:
    print(f"No, {year} is not a leap Year.")