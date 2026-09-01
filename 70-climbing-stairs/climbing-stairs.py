class Solution:
    def climbStairs(self, n: int) -> int:
    #     if n==1 or n==0:
    #         return 1
    #     return self.climbStairs(n-1)+self.climbStairs(n-2)
    
        dp=[-1]*(n+1)
        return self.count(n,dp)
    
    def count(self,n,dp):
        if n==0 or n==1:
            return 1
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.count(n-1,dp)+self.count(n-2,dp)
        return dp[n]