# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         nums=fruits
#         max_length=0
#         freq={}
#         l=0
#         r=0
#         while r<len(fruits):
#             freq[nums[r]]=freq.get(nums[r],0)+1

#             while len(freq) > 2:
#                 freq[nums[l]] -=1

#                 if freq[nums[l]]==0:
#                     del freq[nums[l]]
#                 l+=1

#             if len(freq)<=2:
#                 max_length=max(max_length, r-l+1)
#             r+=1
#         return max_length

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        nums=fruits
        max_length=0
        freq={}
        l=0
        r=0
        while r<len(fruits):
            freq[nums[r]]=freq.get(nums[r],0)+1

            if len(freq) > 2:
                freq[nums[l]] -=1

                if freq[nums[l]]==0:
                    del freq[nums[l]]
                l+=1

            if len(freq)<=2:
                max_length=max(max_length, r-l+1)
            r+=1
        return max_length
