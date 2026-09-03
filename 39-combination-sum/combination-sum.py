class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        queue = [ ([], 0, 0) ]
        while queue:
            arr_ans, current_sum, start = queue.pop(0) 
            if current_sum == target:
                ans.append(arr_ans)
                continue
            if current_sum < target:
                for i in range(start, len(candidates)):
                    num = candidates[i]
                    queue.append((arr_ans + [num], current_sum + num, i))

        return ans
        
        