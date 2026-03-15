from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num=Counter(nums)
        found=False
        for j in num.values():
            if j>1:
                found=True
                break
            else:
                found=False
        
        return True if found else False
            