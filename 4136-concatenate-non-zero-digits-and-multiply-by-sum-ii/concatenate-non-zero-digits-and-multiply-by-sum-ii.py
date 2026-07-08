class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod=10**9+7
        solendivar=(s,queries)
        d=[]
        pos=[]
        for i,c in enumerate(s):
            if c!='0':
                d.append(int(c))
                pos.append(i)
        n=len(d)
        p10=[1]*(n+1)
        pre=[0]*(n+1)
        sm=[0]*(n+1)
        for i in range(n):
            p10[i+1]=p10[i]*10%mod
            pre[i+1]=(pre[i]*10+d[i])%mod
            sm[i+1]=sm[i]+d[i]
        first=[n]*len(s)
        j=0
        for i in range(len(s)):
            while j<n and pos[j]<i:
                j+=1
            first[i]=j
        last=[-1]*len(s)
        j=n-1
        for i in range(len(s)-1,-1,-1):
            while j>=0 and pos[j]>i:
                j-=1
            last[i]=j
        ans=[]
        for l,r in queries:
            i=first[l]
            j=last[r]
            if i>j:
                ans.append(0)
                continue
            x=(pre[j+1]-pre[i]*p10[j-i+1])%mod
            ans.append(x*(sm[j+1]-sm[i])%mod)
        return ans