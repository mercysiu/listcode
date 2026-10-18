class Solution(object):
    def reverseBits(self, n):
        bit_str = "{:032b}".format(n)
        # f"{n:032b}" them so 0 cho du 32 neu chua du do dai, 32 la do dai cua chuoi ke qua ,b la binary
        reverse_bit = bit_str[::-1]
        return int(reverse_bit, 2)

        
                   
         
        