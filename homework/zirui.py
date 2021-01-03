year = int(input("Enter year: "))
month = input("Enter month: ")
day = int(input("Enter day: "))

if year % 100 == 0 and year % 400 == 0:
    leap_year = True
elif year % 100 == 0 and year % 4 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False

if leap_year is True:
    days_of_year = 366
    feb_days = 29
else:
    days_of_year = 365
    feb_days = 28

if month == "Jan" or month == "Mar" or month == "May" or month == "Jul" or month == "Aug" or month == "Oct" or month == "Dec":
    days_of_month = 31
elif month == "Feb":
    if leap_year is True:
        days_of_month = 29
    else:
        days_of_month = 28
else:
    days_of_month = 30

days_before_in_month = day - 1
if month == "Jan":
    print(days_before_in_month)
if month == "Feb":
    print(days_before_in_month + 31)
if month == "Mar":
    print(days_before_in_month + feb_days + 31)
if month == "Apr":
    print(days_before_in_month + feb_days + 31 + 31)
if month == "May":
    print(days_before_in_month + feb_days + 31 + 31 + 30)
if month == "Jun":
    print(days_before_in_month + feb_days + 31 + 31 + 30 + 31)
if month == "Jul":
    print(days_before_in_month + feb_days + 31 + 31 + 30 + 31 + 30)
if month == "Aug":
    print(days_before_in_month + feb_days + 31 + 31 + 30 + 31 + 30 + 31)
if month == "Sep":
    print(days_before_in_month + feb_days + 31 + 31 + 30 + 31 + 30 + 31 + 31)
if month == "Oct":
    print(days_before_in_month + feb_days + 31 + 31 + 30 + 31 + 30 + 31 + 31 + 30)
if month == "Nov":
    print(days_before_in_month + feb_days + 31 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31)
if month == "Dec":
    print(days_before_in_month + feb_days + 31 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30)
