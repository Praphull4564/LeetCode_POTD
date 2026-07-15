class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*n for i in range(n)]
        def solve(i,j):
            if i>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            res=0
            if j==-1:
                res=solve(i+1,i)
            else:
                if prices[i]>prices[j]:
                    p=prices[i]-prices[j]
                    res=p+solve(i+2,-1)
            res=max(res,solve(i+1,j))
            dp[i][j]=res
            return dp[i][j]
            
        return solve(0,-1)



        