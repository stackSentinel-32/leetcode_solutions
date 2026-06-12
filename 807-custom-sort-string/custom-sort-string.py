class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        res=[]
        
        for ch in order:
            if ch in freq:
                res.append(ch*freq[ch])
                del freq[ch]
        
        for ch, fre in freq.items():
            res.append(ch*fre)

        return "".join(res)