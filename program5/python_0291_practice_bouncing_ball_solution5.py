
def find_last_fall_down_height(bouncing_times):

    # base condition
    if bouncing_times == 1:
        return 100

    # resursive call
    # the fall down height of the ball (3rd fall down)  is half of   the fall down height of the ball (2nd fall down)
    return find_last_fall_down_height(bouncing_times - 1) / 2


for i in range(1, 11):
    last_height = find_last_fall_down_height(i)
    print(f"Bouncing time: {i}. last height: {last_height}m")


'''
Summary:

1) how to define the function -> find the answer from the question itself
2) base case
3) state transition -> problem convert to same nature subproblem.
   
'''