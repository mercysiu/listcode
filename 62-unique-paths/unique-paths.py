import math
class Solution(object):
    def uniquePaths(self, m, n):
        #case1
        SoT = math.factorial(m + n -2)
        k = math.factorial(m -1)
        neg = math.factorial(n-1)
        return (SoT)/(k*neg)

        