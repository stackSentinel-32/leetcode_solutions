class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # and_check = (1 << 32) - 1
        # for i in range(left,right+1):
        #     and_check&=i
        #     if and_check==0:
        #         break
        # return and_check
            
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift