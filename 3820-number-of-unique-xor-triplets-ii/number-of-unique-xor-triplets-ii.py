class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        mx = max(nums) << 1

        pair_xor = [False] * mx
        for a in nums:
            for b in nums:
                pair_xor[a ^ b] = True

        ans = [0] * mx
        for x in range(mx):
            if pair_xor[x]:
                for c in nums:
                    ans[x ^ c] = 1

        return sum(ans)