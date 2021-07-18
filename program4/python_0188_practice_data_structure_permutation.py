
'''
Requirement:
Find all 3 number permutation possibilities for number 1, 2, 3, 4, 5

Your program should output all 60 possibilities, as below:
There are total 60 groups. They are: {(5, 4, 2), (1, 5, 4), (2, 1, 3), (4, 2, 1), (2, 5, 1), (3, 2, 1), (4, 5, 3), (2, 5, 4), (5, 2, 1), (3, 2, 4), (1, 2, 5), (1, 4, 2), (3, 1, 2), (3, 4, 1), (3, 1, 5), (1, 4, 5), (5, 2, 4), (4, 1, 2), (4, 1, 5), (2, 4, 5), (4, 3, 2), (4, 3, 5), (5, 3, 2), (5, 1, 2), (5, 4, 1), (3, 5, 2), (1, 5, 3), (2, 1, 5), (4, 2, 3), (4, 5, 2), (2, 5, 3), (1, 2, 4), (5, 2, 3), (3, 1, 4), (1, 3, 2), (1, 3, 5), (4, 3, 1), (2, 4, 1), (2, 3, 5), (5, 1, 4), (5, 3, 1), (5, 4, 3), (3, 5, 1), (1, 5, 2), (5, 3, 4), (3, 5, 4), (2, 1, 4), (4, 2, 5), (4, 5, 1), (1, 2, 3), (1, 3, 4), (3, 2, 5), (1, 4, 3), (3, 4, 2), (3, 4, 5), (2, 3, 4), (4, 1, 3), (2, 4, 3), (2, 3, 1), (5, 1, 3)}
'''

# PREPARE DATA BEGIN ===========================================

# I define a set to hold the 5 numbers
number_set = set(range(1, 6))
# print(number_set)

# I define a list to hold all the permutations
final_result_container = list()

# MAIN PROGRAM BEGIN ==========================================
for i in number_set:
    for j in number_set:
        for k in number_set:
            if i != j and i != k and j != k:
                tuple1 = (i, j, k)
                final_result_container.append(tuple1)

print(f"There are total {len(final_result_container)} groups. They are: {final_result_container}")