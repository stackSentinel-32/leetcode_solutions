class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        j=0
        while i<len(s):
            if j<len(t) and t[j]==s[i]:
                j+=1
            i+=1
        
        return len(t)-j

