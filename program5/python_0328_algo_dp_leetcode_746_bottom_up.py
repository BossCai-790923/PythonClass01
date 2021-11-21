
class Solution:

    def minCostClimbingStairs(self, cost):

        # Step 0) assign param to instance variable, so that we can reference it in our dp function
        self.cost = cost

        # step 1) init dp array
        self.dp = [-1 for _ in range(len(cost) + 1)]
        self.dp[0] = 0
        self.dp[1] = 0

        # Step 2) calculate the result
        top_floor = len(cost)
        return self.f(top_floor)

    def f(self, n):

        # base case
        if n == 0 or n == 1:
            return 0

        for i in range(2, n+1):
            min_cost_total_case1 = self.dp[i-2] + self.cost[i-2]
            min_cost_total_case2 = self.dp[i-1] + self.cost[i-1]
            self.dp[i] = min(min_cost_total_case1, min_cost_total_case2)

        return self.dp[n]







# test code --------------------------------------------------
cost = [16, 19, 10, 12, 18]
solution = Solution()
answer = solution.minCostClimbingStairs(cost)
print(answer)
