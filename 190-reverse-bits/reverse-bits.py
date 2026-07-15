# class Solution:
#     def reverseBits(self, n: int) -> int:
#         ans=0

#         for i in range(32):
#             ans=(ans<<1)|(n&1)
#             n>>=1

#         return ans

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1],2)