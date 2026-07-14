class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n        # length of LIS ending at i
        cnt = [1] * n       # number of LIS ending at i

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:

                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]

                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]

        longest = max(dp)

        ans = 0
        for i in range(n):
            if dp[i] == longest:
                ans += cnt[i]

        return ans