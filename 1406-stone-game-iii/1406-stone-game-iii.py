class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        dp=[float(-inf)]*n
        def solve(i):
            if i>=n:
                return 0
            if i==n-1:
                return stoneValue[i]

            if dp[i]!=float('-inf'):
                return dp[i]
            p1=p2=p3=float('-inf')
            p1=stoneValue[i]+min(solve(i+4),solve(i+2),solve(i+3))
            if i+1<n:
                p2=stoneValue[i]+stoneValue[i+1]+min(solve(i+5),solve(i+3),solve(i+4))
            if i+2<n:
                p3=stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]+min(solve(i+6),solve(i+4),solve(i+5))
            dp[i]=max(p1,p2,p3)
            return dp[i]
        pl1=solve(0)
        pl2=sum(stoneValue)-pl1
        if pl1==pl2:
            return 'Tie'
        elif pl1>pl2:
            return 'Alice'
        else:
            return 'Bob'
            