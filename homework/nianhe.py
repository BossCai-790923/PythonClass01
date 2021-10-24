original_height = 100

def ball_height(n):
    if n == 1:
        return original_height
    return ball_height(n-1) / 2
    # return format(original_height / (2**(n)))



def total_distance(n):
    if n == 1:
        return original_height
    return total_distance(n-1) + 2 * ball_height(n)


print(total_distance(10))
print(ball_height(10))