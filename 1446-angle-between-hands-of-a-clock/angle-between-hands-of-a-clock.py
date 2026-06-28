class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h=hour
        m=minutes
        a=m*6
        b=(h%12)*30+m*0.5
        d=abs(a-b)
        return min(d,360-d)