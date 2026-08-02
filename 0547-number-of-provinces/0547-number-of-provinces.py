class Solution:
    def findCircleNum(self, isC: List[List[int]]) -> int:
        adj=[]
        for i in range(len(isC)):
            l=[]
            for j in range(len(isC)):
                if isC[i][j]==1:
                    l.append(j)
            adj.append(l)
        def dfs(adj,i,vis):
            vis[i]=1
            for x in adj[i]:
                if vis[x]==0:
                    dfs(adj,x,vis)
        vis=[0]*len(isC)
        cnt=0
        for i in range(len(vis)):
            if vis[i]==0:
                dfs(adj,i,vis)
                cnt+=1
        return cnt