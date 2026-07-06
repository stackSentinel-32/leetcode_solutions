class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ans=0
        r=0
        for a,b in intervals:
            if b>r:
                ans+=1
                r=b
        return ans