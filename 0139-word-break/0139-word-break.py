class Solution:
    def wordBreak(self, s: str, wD: List[str]) -> bool:
        wD=set(wD)
        dp={}
        n=len(s)
        def solve(x,st):
            if x==n-1:
                if st+s[x] in wD:
                    return True
                else:
                    return False
            if (x,st) in dp:
                return dp[(x,st)]
            s1=False
            if st+s[x] in wD:
                s1=solve(x+1,'')
            s2=solve(x+1,st+s[x])
            dp[(x,st)]=s1 or s2
            return dp[(x,st)]
        return solve(0,'')