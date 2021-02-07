'''
Requirement:
User inputs year / month / day in number into console.
And your program will format the date properly.

For example:

Year: 2021
Month (1-12): 1
Day (1-31): 2
Jan 2nd, 2021

Year: 2021
Month (1-12): 3
Day (1-31): 1
Mar 1st, 2021
'''

'''
logic:

Observation 1：
Program read year / month / day as 3 int value from console

Conclusion 1:
I use 3 input statement to read the 3 values, then use int() to convert to int value

Observation 2:
Program will convert month into month str:
1 -> Jan, 2 -> Feb, .... 12 -> Dec

Conclusion 2:
I can define a list - months, to hold the 12 months' name, and I use month int as index to read the value directly.

Observation 3:
Program will convert day int to day str:
1 -> 1st; 2 -> 2nd; 3 -> 3rd
4 ... 20 -> 4th ... 20th (17 numbers in total, all of them are ended with th)
21 -> 21st; 22 -> 22nd; 23 -> 23rd
24 - 30 -> 24th - 30th (7 numbers in total, all of them are ended with th)
31 -> 31st

Conclusion 3:
I can define a list - day_endings, to hold the 31 days' ending str, and I use day in as index to read the value directly.
'''

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

day_endings = ['st', 'nd', 'rd'] + ['th'] * 17 + ['st', 'nd', 'rd'] + ['th'] * 7 + ['st']

year = int(input("Year: "))
month = int(input("Month (1-12): "))
day = int(input("Day (1-31): "))

# Remember to subtract 1 from month and day to get a correct index
month_str = months[month - 1]
day_str = str(day) + day_endings[day - 1]

print(month_str, day_str + ',' , year)