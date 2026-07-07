class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=s=p=0
        p=1
        while n:
            d=n%10
            s+=d
            if d:
                x+=d*p
                p*=10
            n//=10
        return x*s