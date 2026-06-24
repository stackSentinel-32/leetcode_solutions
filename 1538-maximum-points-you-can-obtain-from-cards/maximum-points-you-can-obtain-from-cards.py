class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # n=len(cardPoints)
        # mx=float('-inf')
        # i=0
        # while i<k+1:
        #     l_sum=sum(cardPoints[:i])
        #     r_sum=sum(cardPoints[n-(k-i):])

        #     mx=max(mx, l_sum + r_sum)
        #     i+=1
        # return mx

        nums=cardPoints
        n=len(nums)
        if n==k:
            return sum(nums)
        
        l_sum=0
        r_sum=0
        for i in range(k):
            l_sum+=nums[i]
        mx=l_sum

        r_idx=n-1
        for i in range(k-1,-1,-1):
            l_sum-=nums[i]
            r_sum+=nums[r_idx]
            mx=max(mx, l_sum+r_sum)
            r_idx-=1

        return mx
        