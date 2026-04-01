class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n=len(nums)
        total_subset=1<<n
        count=0

        for num in range(1,total_subset):
            subset = []

            for j in range(n):
                if num& (1<<j) !=0 :
                    subset.append(nums[j])

            beautiful = True

            for i in range(len(subset)):
                for j in range(i+1, len(subset)):
                    if abs(subset[i]-subset[j]) == k:
                        beautiful = False
                        break
                if not beautiful:
                    break

            if beautiful:
                count += 1

        return count