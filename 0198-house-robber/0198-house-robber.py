class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)

        dp=[-1]*(n+1)
        def solve(i):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]

            s1=nums[i]+solve(i+2)
            s2=solve(i+1)
            dp[i]=max(s1,s2)
            return dp[i]

        return solve(0)
        


