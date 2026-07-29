class Solution:
    LIMIT=10**6+1
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt=Counter(s)

        half=[0]*26
        mid=""

        for c,f in cnt.items():
            half[ord(c)-ord('a')]=f//2
            if f%2:
                mid=c

        if self.countWays(half)<k:
            return ""

        left=[]
        length=sum(half)

        for z in range(length):
            for i in range(26):
                if half[i]==0:
                    continue

                half[i]-=1
                ways=self.countWays(half)

                if ways>=k:
                    left.append(chr(i+ord('a')))
                    break

                k-=ways
                half[i]+=1

        left="".join(left)
        return left+mid+left[::-1]

    def countWays(self,cnt):
        rem=sum(cnt)
        ans=1

        for x in cnt:
            if x:
                ans*=comb(rem,x)
                if ans>=self.LIMIT:
                    return self.LIMIT
                rem-=x

        return ans