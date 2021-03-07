'''

Logic:

There are several boundaries in the question description:
1) 1 million            10%
2) 2 million            7.5%
3) 3rd / 4th million    5%
4) 5th / 6th million    3%
5) 7/8/9/10th million   1.5%
6) remaining            1%

The description can be converted to the table below:

        ====================
        threshold       rate
        ====================
        above			1%
        --------------------
        4 million		1.5%
        --------------------
        2 million		3%
        --------------------
        2 million		5%
  ^     --------------------
  |     1 million		7.5%
  |     --------------------
  |     1 million		10%
----------------------------------------------------------
As profit goes up, the percentage goes down for each tier.
'''

# Step 1) Define a variable profit - I read annual profit from console
profit = int(input("Total profit of the year: "))

# Step 2) Define variable bonus - use float constructor
bonus = float()

# Step 3) Define variable thresholds and rates which represent the table definition above.
thresholds = [1000000, 1000000, 2000000, 2000000, 4000000]
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]

# Then I use variable I defined above.


'''
I need to check whether the profit exceeds the thresholds value.

------------------------------------------------------------------------------------
        MY LOGIC                                        MY CODE
------------------------------------------------------------------------------------

[tier 1]
 
    if profit <= 1,000,000                          if profit <= thresholds[0]:
        bonus = profit * 0.1                            bonus = profit * rates[0]
        finish                                          finish      Mr Fan's hint: exit() after you print the total bonus
        
    if profit > 1,000,000                           if profit > thresholds[0]:
        bonus = 1,000,000 * 0.1                         bonus = thresholds[0] * rates[0]
        profit = profit - 1,000,000                     profit -= thresholds[0]
        go to [tier 2]                                  go to [tier 2]


[tier 2]

    if profit <= 1,000,000                          if profit <= thresholds[1]:
        bonus = bonus + profit * 0.075                  bonus += profit * rates[1]
        finish                                          finish
        
    if profit > 1,000,000                           if profit > thresholds[1]:
        bonus = bonus + 1,000,000 * 0.075               bonus += thresholds[1] * rates[1]
        profit = profit - 1,000,000                     profit -= thresholds[1]
        go to [tier 3]                                  go to [tier 3]

[tier 3]
    ... ...

[tier 4]
    ... ...

[tier 5]
    ... ...

[tier 6]

    bonus = bonus + profit * 0.01                   bonus += profit * rates[5]

'''

# Step 4) Convert the logic to code

# The for loop covers tier 1 to tier 5
for i in range(len(thresholds)): # range(len(thresholds)) -> range(5) -> 0 to 4 -> [tier 1] to tier[5]

    if profit <= thresholds[i]:
        bonus += profit * rates[i]
        print(f"We should keep ${bonus} to out staff for this outlet.")
        exit()

    bonus += thresholds[i] * rates[i]
    profit -= thresholds[i]

# [tier 6]
bonus += profit * rates[5]
print(f"We should keep ${bonus} to out staff for this outlet.")