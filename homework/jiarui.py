"""
Requirement:
A ball free falls from 100m height, each time bounces to half its original height.
Calculate
1) its total travel distance when it touches the ground 10th time.
2) the height of the ball from where it touches the ground 10th time.
"""

# Part 1: Total travel distance of ball


def distCalc(bounce_no, last_height):
    if bounce_no == 1:
        return 100

    else:
        return last_height + distCalc(bounce_no-1, last_height/2)


result = distCalc(10, 100)
print(f"The total travel distance of the ball after 10 bounces is {result}m")


# Part 2: Height of ball


def heightCalc(bounce_no):
    if bounce_no == 1:
        return 100

    else:
        return heightCalc(bounce_no-1) / 2


height = heightCalc(10)
print(f"The height of the ball from where it touches the ground the 10th time is {height}m")

