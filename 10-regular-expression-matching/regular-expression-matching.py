class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp={}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            if j==len(p):
                return i==len(s)

            match=i<len(s) and (s[i]==p[j] or p[j]=='.')

            if j+1<len(p) and p[j+1]=='*':
                ans=dfs(i,j+2) or (match and dfs(i+1,j))
            else:
                ans=match and dfs(i+1,j+1)

            dp[(i,j)]=ans
            return ans
        return dfs(0,0)