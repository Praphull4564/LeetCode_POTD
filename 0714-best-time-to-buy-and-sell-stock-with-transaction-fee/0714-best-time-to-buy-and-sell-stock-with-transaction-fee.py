class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        def solve(i, holding):
            if i == n:
                return 0

            if dp[i][holding] != -1:
                return dp[i][holding]

            if holding == 0:
                buy = -prices[i] + solve(i + 1, 1)
                skip = solve(i + 1, 0)
                ans = max(buy, skip)
            else:
                sell = prices[i] - fee + solve(i + 1, 0)
                hold = solve(i + 1, 1)
                ans = max(sell, hold)

            dp[i][holding] = ans
            return ans

        return solve(0, 0)