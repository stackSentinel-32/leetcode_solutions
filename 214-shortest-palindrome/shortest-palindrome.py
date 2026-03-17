class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if s=="":
            return ""
        rev=s[::-1]
        for i in range(len(s)):
            if s[:len(s)-i]==rev[i:]:
                return rev[:i]+s