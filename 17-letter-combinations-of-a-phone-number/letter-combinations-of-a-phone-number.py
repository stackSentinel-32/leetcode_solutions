class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mp = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        res = []
        self.solve(0,"",digits,mp,res)
        return res

    def solve(self,index,subset,digits,mp,res):
        if index==len(digits):
            res.append(subset)
            return

        letters=mp[digits[index]]

        for ch in letters:
            self.solve(index+1,subset+ch,digits,mp,res)