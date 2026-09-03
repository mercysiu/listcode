import math
class Solution(object):
    def climbStairs(self, n):
        # maxof2 = n//2
        # ans = 0
        # for i in range(1,maxof2+1):
        #     N = math.factorial(n - i)
        #     K = math.factorial(i)
        #     j = math.factorial(n-2*i)
        #     ans =  ans + N/(K*j)
        # return ans + 1
        #fibonacci
        f1 = 0
        f2 = 1 
        fn = 0
        for i in range(n):
            fn = f1 + f2
            f1 = f2
            f2 = fn
        return fn

        