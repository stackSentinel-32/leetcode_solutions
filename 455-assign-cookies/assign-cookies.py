class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # s.sort()
        # g.sort()
        # l,r=0,0
        # c=0
        # while l<len(g) and r<len(s):
        #     if g[l]<=s[r]:
        #         c+=1
        #         l+=1
        #     r+=1
        # return c
        s.sort()
        g.sort()
        l,r=0,0
        c=0
        while l<len(g) and r<len(s):
            if g[l]<=s[r]:
                c+=1
                l+=1
                r+=1
            else:
                r+=1
        return c

