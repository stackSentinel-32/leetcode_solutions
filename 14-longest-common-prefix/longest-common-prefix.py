class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]

        for i in range(1, len(strs)):
            while strs[i][:len(check)] != check:
                check = check[:-1]

        return check