class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:


        m,n=len(matrix),len(matrix[0])

        if m==1 and n==1:
            return int(matrix[0][0])

        elif m==1:
            return max([int(i) for i in matrix[0]])
        elif n==1:
            return max([int(matrix[i][0]) for i in range(m)])

        for i in range(m):
            for j in range(n):
                matrix[i][j]=int(matrix[i][j])
        dp=[[-1]*n for i in range(m)]
        dp[0]=matrix[0]
        for i in range(m):
            dp[i][0]=matrix[i][0]
        res=max([int(i) for i in matrix[0]])
        res=max(res,max([int(matrix[i][0]) for i in range(m)]))
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==1:
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                else:
                    dp[i][j]=0
                res=max(res,dp[i][j])
        return res*res