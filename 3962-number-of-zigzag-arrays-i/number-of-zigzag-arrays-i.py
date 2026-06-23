class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        M = r - l + 1

        dp = [1] * M

        for i in range(1, n):
            ndp = [0] * M
            s = 0

            if i & 1:
                for v in range(M):
                    ndp[v] = s
                    s = (s + dp[v]) % MOD
            else:
                for v in range(M - 1, -1, -1):
                    ndp[v] = s
                    s = (s + dp[v]) % MOD

            dp = ndp

        return (sum(dp) * 2) % MOD