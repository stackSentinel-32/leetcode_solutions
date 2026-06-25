class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq={}
        pos=True
        for i in bills:
            if i==5:
                freq[i]=freq.get(i,0)+1

            elif i==10:
                if freq.get(5,0)==0:
                    pos=False
                    break
                else:
                    freq[i]=freq.get(i,0)+1
                    freq[5]-=1

            elif i==20:
                if freq.get(10,0)>=1 and freq.get(5,0)>=1:
                    freq[10] -=1
                    freq[5] -= 1
                elif freq.get(5,0) >=3:
                    freq[5] -=3
                else:
                    pos = False
                    break

        return pos
        return pos

                    


