class Solution(object):
    def permute(self, nums):
        ans = []
        queue = [([], 0)]
        key_0 = len(nums)
        while queue:
            arr_ans, length = queue.pop(0)
            key_1 = len(set(arr_ans))
            if length == len(nums) and key_1 == key_0:
                ans.append(arr_ans)
            if length < key_0:
                for i in range(0, len(nums)):
                    num = nums[i]
                    queue.append((arr_ans + [num], length+1))
        return ans
            
        