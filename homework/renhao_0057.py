for i in range(-10, -1):
    total_peaches = 1
    total = 0
    peaches_left = 1
    eaten = 0
    for j in range((i + 1), 0):
        total_peaches = ((peaches_left + 1) * 2)
        total = total + total_peaches
        peaches_left = total
        eaten = total - ((total / 2) - 1)
    print(total, eaten, ((total / 2) - 1))
print(1, (1 / 2) + 1, (1 / 2) - 1)