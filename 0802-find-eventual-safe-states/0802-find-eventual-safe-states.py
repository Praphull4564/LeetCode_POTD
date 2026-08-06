class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vis=[False]*len(graph)
        path=[False]*len(graph)

        def dfs(node):
            vis[node] = True
            path[node] = True

            for nei in graph[node]:
                if not vis[nei]:
                    if dfs(nei):
                        return True
                elif path[nei]:
                    return True

            path[node] = False
            return False
        for i in range(len(graph)):
            if not vis[i]:
                dfs(i)
        res=[]
        for i in range(len(graph)):
            if path[i]==False:
                res.append(i)
        return res
