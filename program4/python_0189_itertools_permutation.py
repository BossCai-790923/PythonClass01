
from itertools import permutations

final_result_container = set(permutations(range(1, 6), 3))
print(f"There are total {len(final_result_container)} groups. They are: {final_result_container}")