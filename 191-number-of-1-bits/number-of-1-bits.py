class Solution(object):
    def hammingWeight(self, n):
        hW = 0
        remainder = 0
        if n == 0:
            return 0
        while n >= 1:
            remainder = n % 2
            n = n // 2
            if remainder == 1:
                hW += 1
        return hW
        
        