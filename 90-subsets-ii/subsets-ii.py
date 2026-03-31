class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # result=[]
        # def bt(ind,subset):
        #     if ind >= len(nums):
        #         result.append(subset.copy())
        #         return 
        #     subset.append(nums[ind])
        #     bt(ind+1,subset)
        #     subset.pop()
        #     bt(ind+1,subset)
        # bt(0,[])
        # result=set(tuple(x) for x in result)
        # result=list(list(x) for x in result)
        # return result

        nums.sort()
        result=[]

        def bt(start,subset):
            
            result.append(subset.copy())
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                subset.append(nums[i])
                bt(i+1,subset)
                subset.pop()

        bt(0,[])
        return result