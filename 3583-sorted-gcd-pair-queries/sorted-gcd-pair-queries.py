class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx=max(nums)
        freq=Counter(nums)

        exact=[0]*(mx+1)

        for g in range(mx,0,-1):
            cnt=0
            for m in range(g,mx+1,g):
                cnt+=freq[m]
                exact[g]-=exact[m]
            exact[g]+=cnt*(cnt-1)//2

        prefix=list(accumulate(exact))
        return [bisect_right(prefix,q) for q in queries]