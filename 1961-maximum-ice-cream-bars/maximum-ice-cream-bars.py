class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res=0

        for cost in costs:
            if coins<cost:
                break
            coins-=cost
            res+=1

        return res