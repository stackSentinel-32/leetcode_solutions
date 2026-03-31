class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        total_subset=1<<n
        sum_exor=0
        for i in range(total_subset):
            curr_exor=0
            for j in range(0,n):
                if i & (1<<j) != 0:
                    curr_exor ^= nums[j]
            
            sum_exor+=curr_exor
        return sum_exor
                    
            