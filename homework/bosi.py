# Step 1) Define a variable profit - I read annual profit from console
total = 0.0

# Step 2) Define variable bonus - use float constructor
bonus = 0.0

# Step 3) Define variable thresholds and rates which represent the table definition above.
rates = [0.1, 0.075, 0.05, 0.05, 0.03, 0.03, 0.015, 0.015, 0.015, 0.015, 0.01]

# Then I use variable I defined above.
profit = int(input('profit'))

if profit < 1000000:
    bonus = profit * rates[0]
    print(f'we should keep ${bonus} to our staff for this outlet.')
    exit()

tier_count = int(profit / 1000000)
for tier in range(tier_count):
    bonus_for_the_tier = rates[tier] * 1000000
    bonus += bonus_for_the_tier

profit_above_10_mil = profit % 1000000
bonus += (profit_above_10_mil * rates[tier_count])
print(f'we should keep ${bonus} to our staff for this outlet.')
print(bonus)
