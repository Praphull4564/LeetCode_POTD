class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n,m=len(s),len(t)
        memo={}
        def solve(i,j):
            if j==m:
                return 1
            if i==n:
                return 0
            res=0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i]==t[j]:
               res+=solve(i+1,j+1)
            res+=solve(i+1,j)
            memo[(i,j)]=res
            return memo[(i,j)]
        return solve(0,0)








                

        