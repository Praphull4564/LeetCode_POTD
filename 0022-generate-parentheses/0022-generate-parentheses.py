class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def solve(i,j,s):
            if i==0 and j==0:
                res.append(s)
                return
            if i:
                solve(i-1,j,s+'(')
            if i<j:
                solve(i,j-1,s+')')
        solve(n,n,"")
        return res