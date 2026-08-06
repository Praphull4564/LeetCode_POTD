class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        boss=[[] for i in range(n)]
        for i in range(n):
            if manager[i]!=-1:
                boss[manager[i]].append(i)
        def solve(x):
            if boss[x]==[]:
                return 0
            s=0
            for i in range(len(boss[x])):
                st = informTime[x]+solve(boss[x][i]) 
                s=max(st,s)
            return s
        return solve(headID)