class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        res=[]
        indi=0
        for num in nums:
            indi^=num
        
        diff = indi & -indi
        a=0
        b=0

        for x in nums:
            if x&diff!=0:
                a^=x

            else:
                b^=x

        return [a,b]

                                                                                                                                                                                                                                                                                        