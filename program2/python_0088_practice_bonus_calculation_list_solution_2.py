'''
Requirement:
refactor 0085, using loop - break - else
'''

# Step 1) Define a variable profit - I read annual profit from console
profit = int(input("Total profit of the year: "))

# Step 2) Define variable bonus - use float constructor
bonus = float()

# Step 3) Define variable thresholds and rates which represent the table definition above.
thresholds = [1000000, 1000000, 2000000, 2000000, 4000000]
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]

for i in range(len(thresholds)): # range(len(thresholds)) -> range(5) -> 0 to 4 -> [tier 1] to tier[5]

    if profit <= thresholds[i]:
        bonus += profit * rates[i]
        break

    bonus += thresholds[i] * rates[i]
    profit -= thresholds[i]

# [tier 6]
else:
    bonus += profit * rates[5]

print(f"We should keep ${bonus} to out staff for this outlet.")