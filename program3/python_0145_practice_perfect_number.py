'''
Requirement:
if a number equals to the sum of all of its factors (excluding itself), then the number is called a perfect number
6 is a perfect number, as 6 = 1 + 2 + 3.
Find all perfect number within 1000


Logic:
1) Find all numbers smaller than 1000, so it should be:

    for candidate in range(2, 1001):
        pass


2) For each candidate, we need to check whether it is a perfect number or not. To do that, we need to:

   2.1) Find all factors of the candidate. (1 included, itself not included)

        factor_list = []
        for potential_factor in range(1, candidate):
            if candidate % potential_factor == 0:
                factor_list.append(potential_factor)

   2.2) Check whether their sum equals to candidate or not

        we can just use built-in function sum()


'''

for candidate in range(2, 1001):

    factor_list = []
    for potential_factor in range(1, candidate):
        if candidate % potential_factor == 0:
            factor_list.append(potential_factor)

    if sum(factor_list) == candidate:
        print(candidate)
