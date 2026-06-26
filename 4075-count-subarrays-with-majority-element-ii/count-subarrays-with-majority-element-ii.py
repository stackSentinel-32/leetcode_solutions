from typing import List
from bisect import bisect_left

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pref=[0]
        cur=0

        for x in nums:
            if x==target:
                cur+=1
            else:
                cur-=1
            pref.append(cur)

        vals=sorted(set(pref))
        bit=[0]*(len(vals)+1)

        def update(i):
            while i<len(bit):
                bit[i]+=1
                i+=i&-i

        def query(i):
            s=0
            while i>0:
                s+=bit[i]
                i-=i&-i
            return s

        ans=0
        update(bisect_left(vals,0)+1)

        for i in range(1,len(pref)):
            idx=bisect_left(vals,pref[i])+1
            ans+=query(idx-1)
            update(idx)

        return ans