class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # count=0

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):

        #         if (j-i) != nums[j]-nums[i]:
        #             count+=1

        # return count

        n=len(nums)
        total_pairs = (n*(n-1))//2

        freq={}
        good_pairs=0

        for i in range(n):
            val=i-nums[i]

            if val in freq:
                good_pairs+=int(freq[val])
            
            freq[val]=freq.get(val,0)+1
        
        return total_pairs-good_pairs
        