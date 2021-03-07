user_input = 0
profits = [0.1, 0.075, 0.05, 0.03, 0.015]
millions = [1000000, 2000000, 4000000, 6000000, 10000000]


while user_input != -1:
    x = 0
    i = 0
    bonus = 0
    user_input = int(input("Input profit, -1 to end: "))

    while i <= 4 and user_input > millions[i]:
        bonus += ((millions[i] - x) * profits[i])
        x = millions[i]
        i += 1

    if i != 5:
        bonus += ((user_input - x) * profits[i])
    else:
        bonus += ((user_input - x) * 0.01)

    print_val = format(bonus, '.2f')
    print(f"The total bonus is ${print_val}")

print("Program ended")