class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        hm = dict()

        for u, v in edges:
            hm[u] = hm.get(u, 0) + 1
            hm[v] = hm.get(v, 0) + 1
        
        for key, value in hm.items():
            if value == n:
                return key
