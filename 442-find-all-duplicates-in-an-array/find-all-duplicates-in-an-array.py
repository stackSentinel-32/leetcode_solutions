class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        win={}
        for i in nums:
            win[i]=win.get(i,0)+1

        res=[] 

        for i,cn in win.items():
            if cn==2:
                res.append(i)
                
        return res