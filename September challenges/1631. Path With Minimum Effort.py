# Union-find
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])

        def union(x, y):
            parent[find(y)] = find(x)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        edges = []
        for i in range(m):
            for j in range(n):
                cur_id = i * n + j
                if i > 0:
                    edges.append((cur_id, cur_id - n, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append((cur_id, cur_id - 1, abs(heights[i][j] - heights[i][j - 1])))        
        edges.sort(key=lambda x:x[2])

        ans = 0
        parent = list(range(m * n))
        for edge in edges:
            union(edge[0], edge[1])
            if find(0) == find(m * n - 1):
                ans = edge[2]
                break
        return ans
