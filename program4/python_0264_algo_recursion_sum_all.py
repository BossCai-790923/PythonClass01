def sum_non_recursion(n):
    result = 0
    for i in range(n+1):
        result += i
    return result


def sum_recursion(n):

    # base case:
    if n <= 1:
        return n

    # recursive call
    return n + sum_recursion(n-1)




# you must pass in a non-negative number, I will omit the parameter check
result = sum_non_recursion(100)
print(result)




