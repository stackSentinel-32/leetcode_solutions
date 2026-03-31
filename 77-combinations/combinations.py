class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=list(range(1,n+1))
        total_subset=1<<n
        result=[]

        for num in range(total_subset):
            lst=[]
            if num.bit_count()==k:
                for i in range(n):
                    if num & (1<<i) != 0:
                        lst.append(nums[i])

                result.append(lst)
        return result