class Solution(object):
    def romanToInt(self, s):
        a = 0
        listv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 } 
        b = listv[s[-1]]
        for i in range(0, len(s)-1):
            f = s[i]
            l = s[i+1]
            if listv[f] > listv[l]:
                a += listv[f]
            if listv[f] < listv[l]:
                a -= listv[f]
            if listv[f] == listv[l]:
                a += listv[f]
        return a + b
            
