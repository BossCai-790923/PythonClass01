celebrities_arrival_schedule = [(6, 8), (6, 12), (6, 7), (7, 8),
                                (7, 10), (8, 9), (8, 10), (9, 12),
                                (9, 10), (10, 11), (10, 12), (11, 12)]

celebrities_met = []

for my_arrival in range(12):
    people_met = 0
    for i in range(len(celebrities_arrival_schedule)):
        if celebrities_arrival_schedule[i][0] <= my_arrival:
            if celebrities_arrival_schedule[i][1] >= (my_arrival+1):
                people_met += 1
    celebrities_met.append(people_met)

best_start_time = celebrities_met.index(max(celebrities_met))

print(f"The best time is {best_start_time} to {best_start_time + 1}.")