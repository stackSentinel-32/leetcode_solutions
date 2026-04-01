class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n=len(nums)
        max_or=0
        for i in range(n):
            max_or = max_or | nums[i]
        
        total_subset=1<<n
        result=[]
        count=0
        for i in range(total_subset):
            check_or=0
            for j in range(n):
                if i&(1<<j)!=0:
                    check_or = check_or | nums[j]
                
            if check_or == max_or:
                count+=1
        return count
                
                

                    