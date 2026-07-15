class Solution:
    def numSquares(self, n: int) -> int:
        arr=[]
        for i in range(1,n+1):
            if i**2<=n:
                arr.append(i**2)
            else:
                break
        dp=[float('+inf')]*(n+1)
        dp[0]=0
        for i in range(n + 1):
            for c in arr:
                if i>=c:
                    dp[i] = min(dp[i] , dp[i-c]+1)  
        return dp[n]
