class Solution(object):
    def reverse(self, x):
        n_s = str(x)
        x_moi = ""
        if n_s[0] == '-':
            x_moi = n_s.replace("-", "")
            x_moi = x_moi[::-1]
            x_moi = '-' + x_moi
        else:
            x_moi = n_s[::-1]
        if int(x_moi) < -2147483648 or int(x_moi) > 2147483647:
            return 0
        return int(x_moi)

        
        