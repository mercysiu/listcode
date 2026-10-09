class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1
        con = len(haystack) - len(needle)
        for i in range(0, len(haystack)):
            last_point = i + len(needle)
            if i > con:
                return -1
            if haystack[i] == needle[0]:
                if haystack[i: last_point] == needle:
                    return i
        return -1
            
        
        