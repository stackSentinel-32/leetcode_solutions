from collections import Counter
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # freq=Counter(word)
        # c=0
        # for w in patterns:
        #     ss=True
        #     for ch in w:
        #         if freq[ch] > 0:
        #             ss=True
        #         else:
        #             ss=False
        #             break
        #     if ss==True:
        #         c+=1
        # return c
        c=0
        for p in patterns:
            if p in word:
                c+=1
        return c
                    