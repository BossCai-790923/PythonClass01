day = int(input('day:'))
month = input('month:')
year = int(input('year:'))

if month == 'january':
    month = 0
if month == 'february':
    month = 31
if month == 'march':
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                month = 60
            else:
                month = 59
        else:
            month = 60
    else:
        month = 59
if month == 'april':
    month = 90
if month == 'may':
    month = 120
if month == 'june':
    month = 151
if month == 'july':
    month = 181
if month == 'august':
    month = 212
if month == 'september':
    month = 243
if month == 'october':
    month = 273
if month == 'november':
    month = 304
if month == 'december':
    month = 334

print(day + month)
