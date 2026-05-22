class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_3=[0 for i in range(32)]
        for num in candidates:
            for j in range(32):
                if num&(1<<j)!=0:
                    bit_3[j]+=1
        
        return max(bit_3)
            