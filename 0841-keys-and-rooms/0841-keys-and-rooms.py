class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=[False]*len(rooms)
        def dfs(n):
            if vis[n]:
                return
            vis[n]=True
            for i in rooms[n]:
                if not vis[i]:
                    dfs(i)
        dfs(0)
        for i in vis:
            if i==False:
                return False
        return True
