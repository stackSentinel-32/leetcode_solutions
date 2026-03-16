class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # hashmap={}
        # for i in nums:
        #     hashmap[i]=hashmap.get(i,0)+1
        
        # nums_pro=[]
        # for key,value in hashmap.items():

        pre=1
        res=[1]*len(nums)
        for i,num in enumerate(nums):
            res[i]=pre
            pre=pre*num
        
        post=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*post
            post=post*nums[i]
        
        return res
