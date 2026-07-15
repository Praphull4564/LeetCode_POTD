class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)

        dp=[[[-1]*2 for i in range(3)] for i in range(n)]

        def solve(i,t,h):
            if i>=n:
                return 0
            if t==0:
                return 0

            if dp[i][t][h]!=-1:
                return dp[i][t][h]

            res=0
            if h==1:
                res = prices[i]+solve(i+1,t-1,0)
                res=max(res,solve(i+1,t,1))
            else:
                res=-prices[i]+solve(i+1,t,1)
                res=max(res,solve(i+1,t,0))

            dp[i][t][h]=res
            return dp[i][t][h]

        return solve(0,2,0)




            