class Solution(object):
    def addDigits(self, num):
        if (num // 2) < 5:
            return num
        nums = 0
        for digit in str(num):
            nums = nums + int(digit)
        return self.addDigits(nums)

        
        