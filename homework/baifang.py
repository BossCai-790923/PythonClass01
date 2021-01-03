# Teacher comments: This part is great, you define a class which holds a date's year/month/day info
class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

# Teacher comments: This part is great, you use a list to contain non-leap year's months' day count
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]


# Teacher comments: This method seems confusing. I am not sure what's the purpose of this method.
def countLeapYears(d):
    years = d.y

    if (d.m <= 2):
        years -= 1

    return int(years / 4) - int(years / 100) + int(years / 400)
# I would suggest, the method's function should tell us whether a date is a leap year or not
# def is_leap_year(d):
#     if d is in a leap year, return True, otherwise return False


# Teacher comments: This method seems confusing. I am not sure what's the purpose of this method.
# This method seems like to calculate the day differences between 2 dates.
# We don't need this function.
# As the homework requirement is: tell what's the total number of days in front of the date which user inputs.
# So we don't need 2 dates, we only need 1 date.
# I would suggest remove this method.
def getDifference(dt1, dt2):
    n1 = dt1.y * 365 + dt1.d

    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]

    n1 += countLeapYears(dt1)

    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)

    return (n2 - n1)


# This function tell you whether the date 'd' is in a leap year or not
# For now, let's just bindly return True
def is_leap_year(d):
    return True


# Teacher's comments: Your question is You don't know how to let user input year/month/day.
# It can simply do in this way:
years = int(input('years: '))
month = int(input('month: '))
days = int(input('days: '))

# After this, you can build a Date object.
date_var = Date(days, month, years)
leap_year_var = is_leap_year(date_var)
print(f"The date_var is in a leap year? {leap_year_var}")

#Once you build this date_var object, what do you do with it?
# I think
# Step 1) call function is_leap_year(date_var) to tell you whether the year is a leap year or not
# Step 2) calculate what's the total number of days in front of the date_var(included) for the year
