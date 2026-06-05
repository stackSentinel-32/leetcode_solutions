class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        taken=set()
        res=0

        for right in range(len(s)):
            while s[right] in taken:
                taken.remove(s[left])
                left+=1
            taken.add(s[right])
            res=max(res,right-left+1)
        return res