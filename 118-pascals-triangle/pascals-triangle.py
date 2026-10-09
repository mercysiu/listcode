class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        if numRows > 2:
            queue = [([1,1], 1)]
            ans = [[1],[1,1]]
            while queue:
                arr,t = queue.pop(0)
                if t > (numRows - 2):
                    return ans
                val = [1]
                for i in range(0, len(arr) - 1):
                    x = arr[i] + arr[i+1]
                    val.append(x)
                val.append(1)
                ans.append(val)
                queue.append((val, t + 1))




        