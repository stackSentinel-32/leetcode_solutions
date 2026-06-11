class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ct=0
        tw=0
        for c in customers:
            ct=max(ct,c[0]) +c[1]
            tw+=ct-c[0]
        return tw/len(customers)