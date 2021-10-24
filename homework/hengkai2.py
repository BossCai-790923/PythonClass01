def result(value, amount, a = 0):
    while a != amount:
        a = a + 1
        value = value / 2
        print(value)
if __name__ == '__main__':
    result(100, 10)
