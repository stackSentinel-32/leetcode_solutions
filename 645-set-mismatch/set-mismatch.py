class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        dup,mis=0,0
        for i in range(1,len(nums)+1):
            if freq.get(i,0)==2:
                dup=i

            if freq.get(i,0)==0:
                mis=i
        return [dup,mis]

            
