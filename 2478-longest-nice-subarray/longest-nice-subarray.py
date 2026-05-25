class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        current_bits = 0
        max_length = 1

        for right in range(len(nums)):

            while current_bits & nums[right]:
                current_bits ^= nums[left]
                left += 1

            current_bits |= nums[right]

            window_size = right - left + 1
            max_length = max(max_length, window_size)

        return max_length