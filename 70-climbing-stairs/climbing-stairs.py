class Solution:
    def climbStairs(self, n: int) -> int:

        prev2=1
        prev1=1
        for i in range(2,n+1):
            curr=prev2+prev1
            prev2=prev1
            prev1=curr
        return prev1
        # dp=[0]*(n+1)
        # dp[0]=1
        # dp[1]=1

        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]


    #     if n==1 or n==0:
    #         return 1
    #     return self.climbStairs(n-1)+self.climbStairs(n-2)
    
    #     dp=[-1]*(n+1)
    #     return self.count(n,dp)
    
    # def count(self,n,dp):
    #     if n==0 or n==1:
    #         return 1
    #     if dp[n]!=-1:
    #         return dp[n]
    #     dp[n]=self.count(n-1,dp)+self.count(n-2,dp)
    #     return dp[n]

    