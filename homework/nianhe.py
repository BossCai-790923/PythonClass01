def recursion(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return recursion(n - 1) + recursion(n - 2)


def non_recursion(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    first = 0
    second = 1
    ans = 0
    for i in range(n - 2):
        ans = first + second
        first = second
        second = ans
    return ans


print(recursion(10))
print(non_recursion(10))