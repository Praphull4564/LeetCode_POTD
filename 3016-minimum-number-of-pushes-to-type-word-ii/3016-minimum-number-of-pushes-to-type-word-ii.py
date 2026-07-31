class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            if i in d:
                d[i][1]+=1
            else:
                d[i]=[i,1]
        v=list(d.values())
        v.sort(key = lambda x:x[1],reverse=True)
        d={}
        for i in v:
            if len(d)<8:
                d[i[0]]=1
            elif len(d)<16:
                d[i[0]]=2
            elif len(d)<24:
                d[i[0]]=3
            else:
                d[i[0]]=4
        res=0
        for i in word:
            res+=d[i]
        return res
        