class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)
        def solve(i):
            if i+2==n:
                return cost[i]
            if i+1==n:
                return cost[i]
            if dp[i]!=-1:
                return dp[i]
            s1=cost[i]+solve(i+2)
            s2=cost[i]+solve(i+1)
            dp[i]=min(s1,s2)
            return dp[i]
        return min(solve(0),solve(1))

