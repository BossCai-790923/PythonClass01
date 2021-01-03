
year = int(input("Year:"))
month = int(input("Month:"))
day = int(input("Day:"))

print(year,"-",month,"-",day)

total_days = 0

# Step 1) add whole months' day count
if month > 1:
    total_days += 31
if month > 2:
    total_days += 28
if month > 3:
    total_days += 31
if month > 4:
    total_days += 30
if month > 5:
    total_days += 31
if month > 6:
    total_days += 30
if month > 7:
    total_days += 31
if month > 8:
    total_days += 31
if month > 9:
    total_days += 30
if month > 10:
    total_days += 31
if month > 11:
    total_days += 30

total_days += day

#Step 2) Check leap year
leap_year = False

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    leap_year = True

if leap_year and month > 2:
    total_days += 1


print("Total days: ", total_days)






