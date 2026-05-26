class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        p_count = {}
        window = {}

        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        k = len(p)

        for i in range(len(s)):
            window[s[i]] = window.get(s[i], 0) + 1

            if i >= k:
                left_char = s[i-k]

                if window[left_char] == 1:
                    del window[left_char]
                else:
                    window[left_char] -= 1

            if window == p_count:
                res.append(i-k+1)

        return res