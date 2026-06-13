class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # maxi=0
        # for i in range(len(nums)):
        #     zeros=0
        #     for j in range(i,len(nums)):
        #         if nums[j]==0:
        #             if zeros>=k:
        #                 break
        #             zeros+=1
        #         maxi=max(maxi,j-i+1)
        # return maxi

        maxi=0
        l=0
        r=0
        zeros=0
        n=len(nums)
        
        # while r<n:
        #     if nums[r]==0:
        #         zeros+=1

        #     while zeros>k:
        #         if nums[l]==0:
        #             zeros-=1
        #         l+=1
            
        #     maxi=max(maxi,r-l+1)
        #     r+=1
        # return maxi
        
        
        while r<n:
            if nums[r]==0:
                zeros+=1

            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            
            if zeros<=k:
                maxi=max(maxi,r-l+1)
            r+=1
        return maxi

        
           