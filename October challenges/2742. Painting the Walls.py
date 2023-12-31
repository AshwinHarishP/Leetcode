from functools import lru_cache

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N = len(cost)
        INF = 10 ** 20

        @lru_cache(None)  # Using lru_cache for memoization
        def calc(ctime, index):
            if ctime >= N:
                return 0
            if index == N:
                return INF

            return min(calc(ctime + time[index] + 1, index + 1) + cost[index], calc(ctime, index + 1))

        # Initialize the best cost to a large value
        best = INF

        # Call the calc function to find the minimum cost
        best = min(best, calc(0, 0))

        return best
 
