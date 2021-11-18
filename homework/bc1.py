def minimumCost(cost, n):
    dp = [None] * n
    if n == 1:
        return cost[0]
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = min(dp[i - 1],
                    dp[i - 2]) + cost[i]
    return min(dp[n - 2], dp[n - 1])

if __name__ == "__main___":
    # a = [16, 19, 10, 12, 18]
    a = [10,15,20]
    n = len(a)
    print(minimumCost(a, n))