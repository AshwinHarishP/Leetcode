class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited[node] = 1
            for i in adjLs[node]:
                if not visited[i]:
                    dfs(i)
        n = len(isConnected)
        visited = [0] * n
        cnt = 0
        adjLs = [[]for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    adjLs[i].append(j)
                    adjLs[j].append(i)

        for i in range(n):
            if not visited[i]:
                cnt += 1
                dfs(i)
        return cnt


        
