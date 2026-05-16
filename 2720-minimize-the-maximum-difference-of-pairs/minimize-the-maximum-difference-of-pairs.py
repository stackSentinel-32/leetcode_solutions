class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        low=0
        high=nums[-1]-nums[0]
        res=high

        while low<=high:
            mid=(low+high)//2
            count=0
            i=0
            while i<len(nums)-1:
                if nums[i+1]-nums[i]<=mid:
                    count+=1
                    i+=2   
                else:
                    i+=1

            if count>=p:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res