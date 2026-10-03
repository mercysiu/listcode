class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s) == 1:
            return 1
        a = 0
        last = 0
        for i in range(1, len(s) + 1):
            if s[-i] != " ":
                a += 1
                    
                if i == len(s) or s[-i -1] == " ":
                    return a    
        return a
        