class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_32=[0 for i in range(32)]

        for num in candidates:
            for j in range(32):
                if num&(1<<j)!=0:
                    bit_32[j]+=1
        
        maxi=float('-inf')
        for i in bit_32:
            maxi=max(i,maxi)
        return  maxi
            