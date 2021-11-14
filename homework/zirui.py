# top-down

memory = [-1] * 50


def fibonacci_rabbit_top_down(num):
    if memory[num] == -1:
        if num == 0:
            memory[num] = 0
        elif num == 1:
            memory[num] = 1
        elif num == 2:
            memory[num] = 1
        elif num == 3:
            memory[num] = 1
        else:
            memory[num] = fibonacci_rabbit_top_down(num - 2) + fibonacci_rabbit_top_down(num - 3) + fibonacci_rabbit_top_down(num - 4)

    return memory[num]


print(fibonacci_rabbit_top_down(20))