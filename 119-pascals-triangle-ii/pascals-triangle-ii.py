class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex  >= 1:
            queue = [([1,1], 1)]
            while queue:
                arr,t = queue.pop(0)
                if t == rowIndex:
                    return arr
                val = [1]
                for i in range(0, len(arr) - 1):
                    x = arr[i] + arr[i+1]
                    val.append(x)
                val.append(1)
                queue.append((val, t + 1))
      