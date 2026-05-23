class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        total_xor = 0
        for x in nums:
            total_xor ^= x
        mask = (1 << maximumBit) - 1
        ans = []

        for i in range(len(nums)):
            ans.append(total_xor ^ mask)
            total_xor ^= nums[len(nums) - 1 - i]
        return ans