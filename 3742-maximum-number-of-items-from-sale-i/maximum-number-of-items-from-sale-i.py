class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:

        n = len(items)

        free_count = [0] * n

        for i in range(n):
            fi = items[i][0]

            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    free_count[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):

            price = items[i][1]
            gain = 1 + free_count[i]

            ndp = dp[:]

            for spent in range(budget - price + 1):

                if spent and dp[spent] == 0:
                    continue

                ndp[spent + price] = max(
                    ndp[spent + price],
                    dp[spent] + gain
                )

            for money in range(price, budget + 1):
                ndp[money] = max(
                    ndp[money],
                    ndp[money - price] + 1
                )

            dp = ndp

        return max(dp)