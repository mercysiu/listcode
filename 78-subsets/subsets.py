class Solution(object):
  def subsets(self, nums):
    ans = []
    queue = [([], 0)]
    while queue:
      arr_ans, start = queue.pop(0)
      ans.append(arr_ans)
      for i in range(start, len(nums)):
        queue.append((arr_ans + [nums[i]], i + 1))
    return ans