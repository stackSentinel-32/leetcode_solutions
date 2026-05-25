class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        if num1==num2:
            return num1
            
        shift=0
        for i in range(32):
            if (num2 & (1<<i)) != 0:
                shift+=1
        
        ans=0
        i=31
        while shift>0 and i>-1:
            if (num1 & (1<<i)) != 0:
                    ans |= (1<<i)
                    shift-=1
            i-=1
        if shift==0:
            return ans
        else:
            for i in range(32):
                if shift > 0 and (ans & (1 << i)) == 0:
                    ans |= (1 << i)
                    shift -= 1
            return ans        