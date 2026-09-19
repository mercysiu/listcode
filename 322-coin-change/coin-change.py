class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for cap in range(1, amount + 1):
            for coin in coins:
                if cap >= coin:
                    dp[cap] = min(dp[cap], dp[cap - coin] + 1)
        if dp[amount] <= amount:
            return dp[amount]
        else:
            return -1
        