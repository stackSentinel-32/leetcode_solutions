class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"

        for _ in range(n-1):
            res=""
            i=0

            while i<len(s):
                cnt=1
                while i+1<len(s) and s[i]==s[i+1]:
                    cnt+=1
                    i+=1

                res+=str(cnt)+s[i]
                i+=1
            s=res

        return s