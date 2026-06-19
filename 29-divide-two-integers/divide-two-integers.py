class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        divd=dividend
        div=divisor
        mx=2**31-1
        mn=-2**31
        if divd==mn and div== -1:
            return mx
        
        sign= -1 if (divd<0)^(div<0) else 1

        divd=abs(divd)
        div=abs(div)

        res=0
        while divd>=div:
            temp=div
            mul=1

            while divd>=(temp<<1):
                temp<<=1
                mul<<=1

            divd-=temp
            res+=mul
        return res if sign>0 else -res
        