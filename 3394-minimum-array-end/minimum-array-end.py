class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # req=[]
        # for i in range(32):
        #     if x&(1<<i):
        #         req.append(i)
        # # print(req)
        # if n==1:
        #     return x

        # nc=1
        # res=[]
        # j=x+1
        # while True:
        #     if all(j&(1<<r) for r in req):
        #         res.append(j)
        #         nc += 1
        #         if nc == n:
        #             break
        #     j+=1
        # return res[-1]

        bit_fill=n-1
        res=x
        x_bit_pos=0

        while bit_fill>0:
            if (res&(1<<x_bit_pos))==0:
                if bit_fill&1:
                    res |= (1<<x_bit_pos)
                bit_fill>>=1
            x_bit_pos+=1

        return res