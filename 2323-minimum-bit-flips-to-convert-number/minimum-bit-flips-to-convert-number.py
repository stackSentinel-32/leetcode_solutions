class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor=start^goal
        count=0
        for i in range(32):
            if xor&(1<<i)!=0:
                count+=1
        return count
