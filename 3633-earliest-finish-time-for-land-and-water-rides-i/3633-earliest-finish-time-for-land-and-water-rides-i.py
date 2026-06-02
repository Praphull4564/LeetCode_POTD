class Solution:
    def earliestFinishTime(self,lST: List[int],lD: List[int],wST: List[int],wD: List[int]) -> int:
        
        res=float("inf")
        for i in range(len(lST)):
            x=lST[i]
            y=lD[i]
            tt=x+y
            for j in range(len(wST)):
                s=wST[j]
                t=wD[j]
                x=0
                if s<=tt:
                    x+=t
                    res=min(res,tt+x)
                else:
                    x+=(s-tt)+t
                    res=min(res,tt+x)



        for i in range(len(wST)):
            x=wST[i]
            y=wD[i]
            tt=x+y
            for j in range(len(lST)):
                s=lST[j]
                t=lD[j]
                x=0
                if s<=tt:
                    x+=t
                    res=min(res,tt+x)
                else:
                    x+=(s-tt)+t
                    res=min(res,tt+x)

        return res


