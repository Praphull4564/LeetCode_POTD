class Solution:
    def maxDepth(self, s: str) -> int:
        cnt=0
        res=0
        x=""
        for i in s:
            if i=='(':
                cnt+=1
            elif i==')':
                res=max(res,cnt)
                cnt-=1
            else:
                continue
        return res