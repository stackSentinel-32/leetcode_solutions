class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq={}
        for i in s1.split():
            freq[i]=freq.get(i,0)+1
        for j in s2.split():
            freq[j]=freq.get(j,0)+1
        
        res=[]
        for i,j in freq.items():
            if j==1:
                res.append(i)
        return res    

        