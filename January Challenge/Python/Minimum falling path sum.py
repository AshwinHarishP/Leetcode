class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[int(1e9) for _ in range(m+1)] for _ in range(n+1)]

        def func(r, c, dp):
            for j in range(m):
                dp[n-1][j] = matrix[n-1][j]

            for i in range(n-2, -1, -1):
                for j in range(m-1, -1, -1): 
                    ld, rd, below = int(1e9), int(1e9), int(1e9)
                    if i + 1 < n and j - 1 >= 0:  
                        ld = matrix[i][j] + dp[i+1][j-1]

                    if i + 1 < n and j + 1 < m:  
                        rd = matrix[i][j] + dp[i+1][j+1]

                    if i + 1 < n: 
                        below = matrix[i][j] + dp[i+1][j]

                    dp[i][j] = min(ld, rd, below)
            return dp[r][c]

        mini = int(1e9)
        for i in range(m):
            res = func(0, i, dp)
            mini = min(mini, res)
        return mini
