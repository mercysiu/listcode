class Solution(object):
    def lengthOfLIS(self, nums):
        length = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    length[i] = max(length[i], length[j] +1)
        return max(length)