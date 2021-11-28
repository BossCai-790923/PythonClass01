class Solution:

    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            dp[i] = min(dp[i-c] if i - c >= 0 else float("inf") for c in coins) + 1

        return dp[-1] if dp[-1] != float("inf") else -1