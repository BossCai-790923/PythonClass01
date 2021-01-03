year = int(input("Which year is it? (exit) "))
month_days = 0

if year == 'exit':
    print(f' ')
while year != 'exit':
    month = input("Which month is it? (jan/feb/mar/apr/may/jun/jul/aug/sep/oct/nov/dec)")
    day = input("Which day is it? ")
    if month == 'jan':
        month_days = 0
    elif month == 'feb':
        month_days = 31
    elif month == 'mar':
        month_days = 31 + 28
    elif month == 'apr':
        month_days = 31 + 28 + 31
    elif month == 'may':
        month_days = 31 + 28 + 31 + 30
    elif month == 'jun':
        month_days = 31 + 28 + 31 + 30 + 31
    elif month == 'jul':
        month_days = 31 + 28 + 31 + 30 + 31 + 31
    elif month == 'aug':
        month_days = 31 + 28 + 31 + 30 + 31 + 31 + 30
    elif month == 'sep':
        month_days = 31 + 28 + 31 + 30 + 31 + 31 + 30 + 31
    elif month == 'oct':
        month_days = 31 + 28 + 31 + 30 + 31 + 31 + 30 + 31 + 30
    elif month == 'nov':
        month_days = 31 + 28 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
    elif month == 'dec':
        month_days = 31 + 28 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 30
    if year % 4 == 0:
        if year % 100 != 0:
            days = int(month_days) + int(day) + 1
            print(f'There are {days} days.')
            year = input("Which year is it? (exit)")
        elif year % 100 == 0:
            if year % 400 == 0:
                days = int(month_days) + int(day) + 1
                print(f'There are {days} days.')
                year = input("Which year is it? (exit)")
            elif year % 400 != 0:
                days = int(month_days) + int(day)
                print(f'There are {days} days.')
                year = input("Which year is it? (exit)")
    elif year % 4 != 0:
        days = int(month_days) + int(day)
        print(f'There are {days} days.')
        year = input("Which year is it? (exit)")
