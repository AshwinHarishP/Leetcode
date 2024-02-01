class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            if node == n-1:
                res.append(path + [node])
                return

            for adj_node in graph[node]:
                dfs(adj_node, path + [node])
        n = len(graph)
        res = []
        path = []

        dfs(0, path)
        return res
