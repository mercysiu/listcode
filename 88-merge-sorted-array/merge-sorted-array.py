class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        return nums1.sort()
        
        