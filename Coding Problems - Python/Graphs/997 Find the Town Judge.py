class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        Indegree = [0] * (n+1)
        Outdegree = [0] * (n+1)
        for u, v in trust:
            Outdegree[u] += 1
            Indegree[v] += 1

        for i in range(1, n+1):
            if Outdegree[i] == 0 and Indegree[i] == n-1:
                return i
        return -1 
