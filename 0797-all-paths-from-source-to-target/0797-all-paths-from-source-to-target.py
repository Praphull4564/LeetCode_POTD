class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        t=len(graph)-1
        def dfs(n,l):
            if n==t:
                nonlocal res
                res.append(l)
                return
            for i in graph[n]:
                dfs(i,l+[i])
            return
        dfs(0,[0])
        return res            



        


