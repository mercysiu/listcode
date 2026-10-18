class Solution(object):
    def intToRoman(self, num):
        nums = num
        ans = ''
        if nums // 1000 > 0:
            ans = 'M' * (nums // 1000)
            nums = nums - 1000 * (nums // 1000)
        if nums // 100 > 0:
            if nums // 100 == 4 or nums // 100 == 9:
                if nums // 100 == 4:
                    ans = ans + 'CD'
                if nums // 100 == 9:
                    ans = ans + 'CM'
            else:
                if nums // 100 == 5:
                    ans = ans + 'D'
                if nums // 100 > 5:
                    ans = ans + 'D' + 'C' * (nums//100 - 5)
                if nums // 100 < 4:
                    ans = ans + 'C' * (nums//100)
            nums = nums - 100 * (nums // 100)
        if nums // 10 > 0:
            if nums // 10 == 4 or nums // 10 == 9:
                if nums // 10 == 4:
                    ans = ans + 'XL'
                if nums // 10 == 9:
                    ans = ans + 'XC'
            else:
                if nums // 10 == 5:
                    ans = ans + 'L'
                if nums // 10 > 5:
                    ans = ans + 'L' + 'X' * (nums//10 - 5)
                if nums // 10 < 4:
                    ans = ans + 'X' * (nums//10)
            nums = nums - 10 * (nums // 10)
        if nums > 0:
            if nums == 4 or nums == 9:
                if nums == 4:
                    ans = ans + 'IV'
                if nums == 9:
                    ans = ans + 'IX'
            else:
                if nums == 5:
                    ans = ans + 'V'
                if nums > 5:
                    ans = ans + 'V' + 'I' * (nums - 5)
                if nums < 4:
                    ans = ans + 'I' * (nums)
        return ans
                                


        


        