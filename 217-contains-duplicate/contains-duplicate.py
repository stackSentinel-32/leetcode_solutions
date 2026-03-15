# from collections import Counter
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         num=Counter(nums)
#         found=False
#         for j in num.values():
#             if j>1:
#                 found=True
#                 break
#             else:
#                 found=False
        
#         return True if found else False
            
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        
        return False
