while True:

    year = (input("Please input year: "))
    if year == 'exit':
        break
    month = (input("Please input month: "))
    day = int(input("Please input day: "))
    year_int = int(year)
    leap_year_determinator = year_int % 4
    number_of_days = 0

    if leap_year_determinator == 0:
        feb = 29

    else:
        feb = 28


    # this is wrong
    if month == 'jan' or 'mar' or 'apr' or 'may' or 'june':
        pass

    # this is correct
    if month == 'jan' or month == 'mar' or month == 'apr' or month == 'may' or month == 'june':
        pass






        if month == 'jan':
            number_of_days += day
        elif month == 'feb':
            number_of_days += day + 31
        elif month == 'mar':
            number_of_days += day + 31 + feb
        elif month == 'apr':
            number_of_days += day + 31 + feb + 31
        elif month == 'may':
            number_of_days += day + 31 + feb + 31 + 30
        elif month == 'june':
            number_of_days += day + 31 + feb + 31 + 30 + 31

    if month == 'july' or 'aug' or 'sep' or 'oct' or 'nov' or 'dec':
        if month == 'july':
            number_of_days += day + 153 + feb
        elif month == 'aug':
            number_of_days += day + 153 + feb + 31
        elif month == 'sep':
            number_of_days += day + 153 + feb + 31 + 31
        elif month == 'oct':
            number_of_days += day + 153 + feb + 31 + 31 + 30
        elif month == 'nov':
            number_of_days += day + 153 + feb + 31 + 31 + 30 + 31
        elif month == 'dec':
            number_of_days += day + 153 + feb + 31 + 31 + 30 + 31 + 30

    print(f"{year} / {month} / {day} has {number_of_days} days in front of it.")
