class Solution:
    def solve(self,index,total,subset,nums,target,result):
        if total== target:
            result.append(subset.copy())
            return 
        elif total>target:
            return
        if index>=len(nums):
            return
        
        summ=total+nums[index]
        subset.append(nums[index])
        self.solve(index,summ,subset,nums,target,result)
        summ=total
        subset.pop()
        self.solve(index+1,summ,subset,nums,target,result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        self.solve(0,0,[],candidates,target,res)
        return res