class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            visited[node] = 1
            adj_room = rooms[node]

            for room in adj_room:
                if not visited[room]:
                    dfs(room)

        n = len(rooms)
        visited = [0]*n

        dfs(0)
        
        for i in range(n):
            if not visited[i]:
                return False
        return True
            
