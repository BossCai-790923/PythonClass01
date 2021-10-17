import time




def count_down(n):

    time.sleep(1)
    print(n)

    # base case
    if n == 0:
        return

    # recursive call
    count_down(n-1)


count_down(10)