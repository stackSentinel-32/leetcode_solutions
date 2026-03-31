class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # n=len(nums)
        # total_subsets=1<<n
        # result=[]

        # for num in range(total_subsets):
        #     lst=[]
        #     for i in range(n):
        #         if num & (1<<i) !=0:
        #             lst.append(nums[i])
        #     result.append(lst)
        # return result

        # n=len(nums)
        # total_subsets=1<<n
        # result=[]

        # for num in range(total_subsets):
        #     lst=[]
        #     for i in range(n):
        #         if (num>>i)&1 !=0:
        #             lst.append(nums[i])
        #     result.append(lst)
        # return result


        result=[]
        
        def bt(ind,subset):
            if ind>=len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[ind])
            bt(ind+1,subset)
            subset.pop()
            bt(ind+1,subset)

        bt(0,[])
        return result
        