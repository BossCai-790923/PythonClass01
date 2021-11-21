'''
https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
'''

'''
-----------------------
cost[i] meaning
-----------------------

index i   means  step i
cost[i]   means  once you stand on step i, you need to pay price cost[i] if you want to leave it for a higher step.
cost[i] is 0-based, meaning 1st step is step 0, not step 1.
to leave step 0 for a higher step like step 1 or step 2, you need to pay cost[0] 
to leave step 5 for a higher step like step 6 or step 7, you need to pay cost[5] 


------------------------------------------------------------------------------
Question 1) How to define the dp function? / What's the meaning of the dp array? 
------------------------------------------------------------------------------

*THE QUESTION ITSELF IS ALREADY THE ANSWER TO 'HOW TO DEFINE YOUR FUNCTION'. *

The question is                                               what's the min cost to reach the top of the floor? 
To rephrase it, or to say, parameterize the question,         what's the min cost to reach step n? 


f(n):
param n     means step n
f(n)        means the min cost to reach step n

there are in total len(cost) steps. The step index ranges from 0 to len(cost) -1; In math we say, [0, len(cost)-1]
So the top of the floor -> len(cost)
so the question is asking you f(len(cost))


our dp array:
dp = []
index i    means step i
dp[i]      means the min cost to reach step i

---------------------------------------------------------------------
Question 2) What's the base case? / How to initialize the dp array?
---------------------------------------------------------------------
You can either start from the step 0 or step 1,
it means, it costs 0 to reach step 0 or step 1, so
f(0) = 0
f(1) = 0

dp = [-1 for _ in range(len(cost) + 1)]
dp[0] = 0
dp[1] = 0

------------------------------------------------------------------------
Question 3) What's the state transition? From THE problem to subproblem?
------------------------------------------------------------------------

To reach step n, you can either come from step n-1 or step n-2

[case 1]
if you come from step n-1, the total cost will be the sum of :
1) min cost to reach step n-1                 -> f(n-1)
2) price you need to pay to leave step n-1    -> cost[n-1]
which is: f(n-1) + cost[n-1]

[case 2]
if you come from step n-2, the total cost will be the sum of :
1) min cost to reach step n-n                 -> f(n-2)
2) price you need to pay to leave step n-2    -> cost[n-2]
which is: f(n-2) + cost[n-2]

so we only need to check which case has a smaller value:
f(n) = Math.min(f(n-1) + cost[n-1], f(n-2) + cost[n-2])

'''

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

        # base case:
        if n == 0 or n == 1:
            return 0

        # recursive call

        # case 1
        if self.dp[n-2] != -1:
            min_cost_to_below_step = self.dp[n-2]
        else:
            min_cost_to_below_step = self.f(n-2)

        min_cost_total_case1 = min_cost_to_below_step + self.cost[n-2]

        # case 2
        if self.dp[n-1] != -1:
            min_cost_to_below_step = self.dp[n-1]
        else:
            min_cost_to_below_step = self.f(n-1)

        min_cost_total_case2 = min_cost_to_below_step + self.cost[n-1]

        min_cost = min(min_cost_total_case1, min_cost_total_case2)

        self.dp[n] = min_cost

        return min_cost


# test code --------------------------------------------------
cost = [16, 19, 10, 12, 18]
solution = Solution()
answer = solution.minCostClimbingStairs(cost)
print(answer)
