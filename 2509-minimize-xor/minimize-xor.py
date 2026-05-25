class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # if num1==num2:
        #     return num1

        # shift=0
        # for i in range(32):
        #     if (num2 & (1<<i)) != 0:
        #         shift+=1
        
        # shift=2
        # set_bit=0
        # i=31
        # while shift>0 and i>-1:
        #     if (num1 & (1<<i)) != 0:
        #             set_bit |= (1<<i)
        #             shift-=1
        #     i-=1
        
        # for i in range(32):
        #     if shift>0 and (set_bit & (1<<i)) == 0:
        #         set_bit |= (1 << i)
        #         shift-=1

        # return set_bit

        # count set bits needed
        shift = bin(num2).count("1")

        ans = 0

        # take matching high bits from num1
        for i in range(31, -1, -1):
            if (num1 & (1 << i)) and shift > 0:
                ans |= (1 << i)
                shift -= 1

        # add remaining bits from low positions
        for i in range(32):
            if shift > 0 and (ans & (1 << i)) == 0:
                ans |= (1 << i)
                shift -= 1

        return ans