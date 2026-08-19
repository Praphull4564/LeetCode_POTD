class Solution:
    def maxNumberOfFamilies(self, n: int, rS: List[List[int]]) -> int:
        d={}
        for i in rS:
            if i[0] in d:
                d[i[0]].add(i[1])
            else:
                d[i[0]]=set([i[1]])
        res=2*(n-len(d))
        for i in d:
            l=d[i]
            t2345=False
            if 2 not in l and 3 not in l and 4 not in l and 5 not in l:
                res+=1
                t2345=True
            t4567=False
            if 7 not in l and 6 not in l and 4 not in l and 5 not in l and not t2345:
                res+=1
                t4567=True
            if 7 not in l and 6 not in l and 8 not in l and 9 not in l and not t4567:
                res+=1
        return res
