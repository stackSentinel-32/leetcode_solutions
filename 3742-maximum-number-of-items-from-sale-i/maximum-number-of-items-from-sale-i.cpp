class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {

        int n = items.size();

        vector<int> free_count(n, 0);

        for (int i = 0; i < n; i++) {
            int fi = items[i][0];

            for (int j = 0; j < n; j++) {
                if (i != j && items[j][0] % fi == 0)
                    free_count[i]++;
            }
        }

        vector<int> dp(budget + 1, 0);

        for (int i = 0; i < n; i++) {

            int price = items[i][1];
            int gain = 1 + free_count[i];

            vector<int> ndp = dp;

            for (int spent = 0; spent + price <= budget; spent++) {

                if (spent && dp[spent] == 0)
                    continue;

                ndp[spent + price] = max(
                    ndp[spent + price],
                    dp[spent] + gain
                );
            }

            for (int money = price; money <= budget; money++) {
                ndp[money] = max(
                    ndp[money],
                    ndp[money - price] + 1
                );
            }

            dp = ndp;
        }

        return *max_element(dp.begin(), dp.end());
    }
};