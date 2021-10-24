bounce = 0
distance = 0
ending_height = 0


def ball_bounce_distance(height):
    global distance
    global bounce
    if bounce == 9:
        return distance*2 - 100
    else:
        bounce += 1
        distance += height
        return ball_bounce_distance(height/2)

#
# def ball_bounce_10_height(height):
#     global bounce
#     global ending_height
#     if bounce == 10:
#         return ending_height
#     else:
#         bounce += 1
#         ending_height = height
#         return ball_bounce_10_height(height/2)


print(ball_bounce_distance(100))
print(distance)
print(bounce)
#
# bounce = 0
# print(ball_bounce_10_height(100))