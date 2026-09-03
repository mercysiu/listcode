class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxn = 0
        while left < right:
            n = min(height[left], height[right]) * (right - left)
            maxn = max(maxn, n)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxn
        
        
      
        

        