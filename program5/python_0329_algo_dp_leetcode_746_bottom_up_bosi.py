'''
the code is given by Bosi, very smart!
'''

class Solution:

    def minCostClimbingStairs(self, cost: list[int]) -> int:

            for i in range(2, len(cost)):
                cost[i] += min(cost[i-1], cost[i-2])

            return min(cost[len(cost)-1], cost[len(cost)-2])

'''
Python allows you to specify the parameter type and return type
for param type, you use : followed by the param type
for return type, you use -> followed by the return type

: list[int]         specify the function param type of cost 
-> int              specify the function return value

'''

# testing code -------------------------------
cost = [16, 19, 10, 12, 18]
solution = Solution()
print(solution.minCostClimbingStairs(cost))
