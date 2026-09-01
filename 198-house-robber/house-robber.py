class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        return self.sol(nums,0,dp)
    
    def sol(self,nums,idx,dp):
        if idx>=len(nums):
            return 0
        if dp[idx]!=-1:
            return dp[idx]
        
        pick=nums[idx]+self.sol(nums,idx+2,dp)

        not_pick=self.sol(nums,idx+1,dp)
        dp[idx]=max(pick,not_pick)
        return dp[idx]
