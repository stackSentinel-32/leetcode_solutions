from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')

        runs = []
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                runs.append((i, j - 1))
                i = j
            else:
                i += 1

        m = len(runs)
        p_arr = [p for p, q in runs]
        q_arr = [q for p, q in runs]

        a_arr = [0] * m 
        b_arr = [0] * m   
        for k in range(m):
            a_arr[k] = 0 if k == 0 else runs[k - 1][1] + 1
            b_arr[k] = (n - 1) if k == m - 1 else runs[k + 1][0] - 1

        full_gain = [(p_arr[k] - a_arr[k]) + (b_arr[k] - q_arr[k]) for k in range(m)]

        if m > 0:
            log_table = [0] * (m + 1)
            for k in range(2, m + 1):
                log_table[k] = log_table[k // 2] + 1

            K = log_table[m] + 1
            sparse = [full_gain[:]]
            for j in range(1, K):
                half = 1 << (j - 1)
                prev = sparse[-1]
                length = m - (1 << j) + 1
                if length <= 0:
                    break
                sparse.append([max(prev[idx], prev[idx + half]) for idx in range(length)])

            def range_max(lo, hi):  
                length = hi - lo + 1
                kk = log_table[length]
                return max(sparse[kk][lo], sparse[kk][hi - (1 << kk) + 1])
        else:
            def range_max(lo, hi):
                return float('-inf')

        ans = []
        for l, r in queries:
            if m == 0:
                ans.append(total_ones)
                continue

            i_low = bisect_right(p_arr, l)          # first run with p > l
            i_high = bisect_left(q_arr, r) - 1       # last run with q < r

            if i_low > i_high or i_low >= m or i_high < 0:
                ans.append(total_ones)
                continue

            if i_low == i_high:
                k = i_low
                gain = (p_arr[k] - max(a_arr[k], l)) + (min(b_arr[k], r) - q_arr[k])
            else:
                k1 = i_low
                gain_low = (p_arr[k1] - max(a_arr[k1], l)) + (b_arr[k1] - q_arr[k1])
                k2 = i_high
                gain_high = (p_arr[k2] - a_arr[k2]) + (min(b_arr[k2], r) - q_arr[k2])
                best = max(gain_low, gain_high)
                if i_high - i_low >= 2:
                    best = max(best, range_max(i_low + 1, i_high - 1))
                gain = best

            ans.append(total_ones + gain)

        return ans