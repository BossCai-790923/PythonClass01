
def howmanyin_no_recursion(target_list):
    return len(target_list)


'''
Summary:
1) Recursion is to convert the problem into a smaller scale sub-problem.
howmanyin(target_list) is converted to 1 + howmanyin(target_list[1:])
'''

def howmanyin(target_list):

    if target_list[1:]: # this equals to      if len(target_list[1:]) != 0:

        # recursive call
        return 1 + howmanyin(target_list[1:])

    else:

        # base case
        return 1


l1 = [n for n in range(10)]
# print(f'list size is {howmanyin_no_recursion(l1)}')
print(f'list size is {howmanyin(l1)}')



