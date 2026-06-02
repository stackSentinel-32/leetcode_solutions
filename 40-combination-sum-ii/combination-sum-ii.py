class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        self.backtrack(0,target,[],candidates,result)
        return result
    
    def backtrack(self,index,total,subset,nums,result):
        if total==0:
            result.append(subset.copy())
            return
        if total<0:
            return 
        if index>=len(nums):
            return 
        
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            tt=total-nums[i]
            self.backtrack(i+1,tt,subset,nums,result)
            subset.pop()



    #     result=set()
    #     candidates.sort()
    #     self.solve(0,0,[],candidates,target,result)
    #     return [list(x) for x in result]

    # def solve (self,index,total,subset,nums,target,result):
    #     if total==target:
    #         result.add(tuple(subset))
    #         return 
    #     elif total>target:
    #         return 
    #     if index>=len(nums):
    #         return 
    #     summ=total+nums[index]
    #     subset.append(nums[index])
    #     self.solve(index+1,summ,subset,nums,target,result)
    #     summ=total
    #     subset.pop()
    #     self.solve(index+1,summ,subset,nums,target,result)
