class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        Indegree = [0] * n
        res = []
        for u, v in edges:
            Indegree[v] += 1
        
        for i in range(len(Indegree)):
            if Indegree[i] == 0:
                res.append(i)
        return res
