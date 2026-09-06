class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n,m=len(s),len(t)
        dp={}
        def solve(i,j):
            if j>=m:
                return 1
            if i>=n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res=solve(i+1,j)
            if s[i]==t[j]:
                res+=solve(i+1,j+1)
            dp[(i,j)]=res
            return res
        return solve(0,0)