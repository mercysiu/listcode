class Solution(object):
    def rob(self, nums):
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            max_val = max(nums[i] + dp(i + 2), dp(i + 1))
            memo[i] = max_val
            return max_val
        return dp(0)