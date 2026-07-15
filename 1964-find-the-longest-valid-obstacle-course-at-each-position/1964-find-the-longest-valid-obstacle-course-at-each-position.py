from bisect import bisect_right as br
class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        n=len(o)
        LIS=[o[0]]
        l=[1]*n
        for i in range(1,n):
            idx=br(LIS,o[i])
            if idx==len(LIS):
                LIS.append(o[i])
                l[i]=len(LIS)
            else:
                LIS[idx]=o[i]
                l[i]=idx+1
        
        return l






        