print(50 * '-')
totalbounce = 0
bounce = 0


def result(value, amount, a=0, Down=False, Up=False):
    global totalbounce
    totalbounce = totalbounce + value / 2 + value
    # print(value)
    while a != amount:
        a = a + 1
        if Down == True:
            value = value / 2
        if Up == True:
            value = value * 2
        totalbounce = totalbounce + value / 2 + value
        # print(value)
    return value


if __name__ == '__main__':
    down = result(100, 10, Down=True)
    print("Total bounce height going down: ")
    print(totalbounce)
    bounce = bounce + totalbounce
    up = result(down, 10, Up=True)
    print("Total bounce height going from up to down: ")
    print(totalbounce)
    bounce = bounce + totalbounce
    print("Total bounce height: ")
    print(bounce)
