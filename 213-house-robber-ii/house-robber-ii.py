class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n==1:
            return nums[0]
        dp=[-1]*(n-1)
        res1=self.sol(nums[0:n-1],0,dp)
        dp=[-1]*(n-1)
        res2=self.sol(nums[1:n],0,dp)
        return max(res1,res2)
    
    def sol(self,nums,idx,dp):
        if idx>=len(nums):
            return 0
        if dp[idx]!=-1:
            return dp[idx]
        
        pick=nums[idx]+self.sol(nums,idx+2,dp)
        not_pick=self.sol(nums,idx+1,dp)
        dp[idx]=max(pick,not_pick)
        return dp[idx]