class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left=0
        # taken=set()
        # res=0

        # for right in range(len(s)):
        #     while s[right] in taken:
        #         taken.remove(s[left])
        #         left+=1
        #     taken.add(s[right])
        #     res=max(res,right-left+1)
        # return res

        # maxi=0
        # for i in range(len(s)):
        #     taken=set()
        #     for j in range(i,len(s)):
        #         if s[j] in taken:
        #             break
        #         maxi=max(maxi,j-i+1)
        #         taken.add(s[j])
        # return maxi

        taken={}
        l=0
        r=0
        maxi=0
        while r<len(s):
            if s[r] in taken:
                l=max(l,taken[s[r]]+1)
            maxi=max(maxi,r-l+1)
            taken[s[r]]=r
            r+=1
        return maxi
