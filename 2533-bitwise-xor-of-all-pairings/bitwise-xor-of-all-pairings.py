class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res=0
        if len(nums1)%2==0 and len(nums2)%2==0:
            return 0
        elif len(nums2)%2==0:
            for num2 in nums2:
                res^=num2
        elif len(nums1)%2==0:
            for num1 in nums1:
                res^=num1
        else:
            for num1 in nums1:
                res^=num1
            for num2 in nums2:
                res^=num2
        return res



        # res=0
        # for num1 in nums1:
        #     for num2 in nums2:
        #         res^=num1^num2

        # return res