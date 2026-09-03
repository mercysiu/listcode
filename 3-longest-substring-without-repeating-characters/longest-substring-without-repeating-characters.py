class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # ans = 0
        # if len(set(s)) == 1:
        #     return 1
        # for i in range(0, len(s)-1):
        #     if s[i] == s[i+1]:
        #         ans = 0
        #     else:
        #         ans += 1
        # return ans
        seen = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1   
            seen[s[right]] = right  
            max_len = max(max_len, right - left + 1)  
        return max_len


        
        