for i in range(1, 10):
    numbers = []
    for j in range(1, i + 1):
        for k in range(i, i + 1):
            numbers.append(str(j) + '*' + str(k) + '=' + str(j * k))
    print(numbers)