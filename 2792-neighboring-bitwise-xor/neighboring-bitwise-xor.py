class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x=0
        for v in derived:
            x^=v
        return x==0