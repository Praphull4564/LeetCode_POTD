class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1=set()
        s2=set()
        res=[]
        for i,j in zip(A,B):
            s1.add(i)
            s2.add(j)
            rx=list(s1&s2)
            res.append(len(rx))
        return res