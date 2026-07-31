class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=sorted(list(d.values()),reverse=True)
        res=0
        for i in range(len(d)):
            if i<8:
                res=res+d[i]*1
            elif i<16:
                res=res+d[i]*2
            elif i<24:
                res=res+d[i]*3
            else:
                res=res+d[i]*4
        return res

