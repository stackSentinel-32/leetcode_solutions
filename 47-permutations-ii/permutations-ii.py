class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        self.solve(nums, [], used, res)
        return res

    def solve(self, nums, subset, used, res):
        if len(subset) == len(nums):
            res.append(subset.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            used[i] = True
            subset.append(nums[i])
            self.solve(nums, subset, used, res)
            subset.pop()
            used[i] = False