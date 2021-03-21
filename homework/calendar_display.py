from datetime import date


def leapyear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def first_day(year, month):
    month_first_day = date(year,month,1)
    day = month_first_day.isoweekday() # Mon - 1; Tue - 2; Wed - 3; Thu - 4; Fri - 5; Sat - 6; Sun - 7
    return day % 7 # This is to make sure Sunday returns 0 not 7.  Sun - 0; Mon - 1; Tue - 2; Wed - 3; Thu - 4; Fri - 5; Sat - 6


month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
def num_days(month, leap):
    if month != 2 or not leap:
        return month_days[month-1]
    return 29


month_str = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def gen_month(month, day_one, month_days):
    result = []
    result.append(month_str[month-1])

    current_line = ''
    curent_line_day_count = 0

    day_list = []
    for space in range(day_one):
        day_list.append(' ')
    day_list.extend(list(range(1, month_days + 1)))

    for day in day_list:
        current_line += str(day)
        current_line += ' ' * (3 - len(str(day)))
        curent_line_day_count += 1
        if curent_line_day_count == 7:
            result.append(current_line)
            current_line = ''
            curent_line_day_count = 0

    result.append(current_line)
    return result


def gen_year(year):
    result = []
    result.append(year)
    for month in range(1, 13):
        result.append(gen_month(month, first_day(year, month), num_days(month, leapyear(year))))
    return result



def display_year(year):
    calendar = gen_year(year)
    print(calendar[0])
    calendar.pop(0)
    for month_calendar in calendar:
        print(month_calendar[0])
        month_calendar.pop(0)
        print("Su Mo Tu We Th Fr Sa")
        for line in month_calendar:
            print(line)
        print("")


# Step 1) Read year from console
year = int(input("Which year of the Calendar you need to see: "))

# Step 2) display year
display_year(year)
