'''
0053 starts from x, check x+100, x+100+168 are square numbers or not.
0054 starts from square numbers. It checks whether any 2 square numbers with a different 168.

Logic:
1) As the max X is 2000, is the max square number should be 2000 + 100 + 168 = 2268, < 2500,
   So the 2 square numbers mentioned above are all less than 50.

2) So all I need to do is to loop all square numbers from 1 - 2500 (1^2 - 50^2)
   See any square number a, plus 168, is that another square number?
   If yes, then the square number a - 100 is what I need.
'''
import math

for sqr_root in range(1,51):
    sqr_num_1 = sqr_root ** 2
    sqr_num_2 = sqr_num_1 + 168

    sqr_root_for_sqr_num_2 = math.sqrt(sqr_num_2)
    sqr_root_for_sqr_num_2_int = int(sqr_root_for_sqr_num_2)

    if sqr_root_for_sqr_num_2 != sqr_root_for_sqr_num_2_int:
        continue  #sqr_num_2 is not a square number.

    print(sqr_num_1 - 100, "is such a number!")
