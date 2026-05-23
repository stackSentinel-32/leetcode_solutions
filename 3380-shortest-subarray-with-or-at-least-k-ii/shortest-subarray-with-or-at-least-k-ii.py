class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bit_count = [0] * 32
        left = 0
        current_or = 0
        ans = float('inf')
        for right in range(n):
            val = nums[right]

            for b in range(32):
                if val & (1 << b):
                    bit_count[b] += 1
                    current_or |= (1 << b)
                    
            while left <= right and current_or >= k:
                ans = min(ans, right - left + 1)
                remove_val = nums[left]

                for b in range(32):
                    if remove_val & (1 << b):
                        bit_count[b] -= 1
                        if bit_count[b] == 0:
                            current_or ^= (1 << b)
                left += 1
        if ans == float('inf'):
            return -1
        return ans


        # n=len(nums)
        # total_subsets=1<<n
        # res=[]
        # for num in range(total_subsets):
        #     l=[]
        #     for i in range(0,n):
        #         if num&(1<<i)!=0:
        #             l.append(nums[i])
        #     if l==[]:
        #         continue
        #     else:
        #         res.append(l)

        # found=False
        # mn=float('inf')
        # for j in res:
        #     or_check=0
        #     for num in j:
        #         or_check |= num

        #     if or_check >k:
        #         found=True
        #         mn=min(mn,len(j))

        # if found:
        #     return mn

        # return -1
             

                