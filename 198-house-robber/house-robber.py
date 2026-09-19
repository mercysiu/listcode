class Solution(object):
    def rob(self, nums):
        memo = {}
        def house(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            max_val = max(nums[i] + house(i + 2), house(i + 1))
            memo[i] = max_val
            return max_val
        return house(0)