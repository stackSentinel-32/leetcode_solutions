class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        nums=[i for i in range(1,10)]
        self.solve(0,0,[],nums,k,n,res)
        return res

    def solve(self,index,total,subset,nums,k,n,res):
        if total==n and len(subset)==k:
            res.append(subset.copy())
            return 
        elif total>n or len(subset)>k:
            return 
        if index>=len(nums):
            return 
        summ=total+nums[index]
        subset.append(nums[index])
        self.solve(index+1,summ,subset,nums,k,n,res)
        summ=total
        subset.pop()
        self.solve(index+1,summ,subset,nums,k,n,res)
        

        
        
               