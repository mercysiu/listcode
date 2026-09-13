import math
class Solution(object):
    def uniquePaths(self, m, n):
        #case1: C(n, k)
        # SoT = math.factorial(m + n -2)
        # k = math.factorial(m -1)
        # neg = math.factorial(n-1)
        # return (SoT)/(k*neg)
        #case2: dynamic programming
        pscase_rn = {}
        def recur(up, left):
            if up < 0 or left < 0:
                return 0
            if up == 0 or left == 0:
                return 1
            if (up, left) in pscase_rn:
                return pscase_rn[(up,left)]
            pscase_rn[(up, left)] = recur(up-1, left) + recur(up, left-1)
            return pscase_rn[(up,left)]
        return recur(m -1, n -1)

            


        