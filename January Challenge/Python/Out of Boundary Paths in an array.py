class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        def helper(i, j, maxMove, dp):

            if i < 0 or j < 0 or i >= m or j >= n:
                return 1

            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            
            Right, Left, Up, Down = 0, 0, 0, 0

            if maxMove > 0:
                Right = helper(i, j+1, maxMove - 1, dp)

            if maxMove > 0:
                Left = helper(i, j-1, maxMove - 1, dp)
            
            if maxMove > 0:
                Up = helper(i-1, j, maxMove - 1, dp)
            
            if maxMove > 0:
                Down = helper(i+1, j, maxMove - 1, dp)
            
            dp[i][j][maxMove] = (Right + Left + Up + Down) % ((10**9) + 7)
            return dp[i][j][maxMove]

        dp = [[[-1 for _ in range(maxMove+1)]for _ in range(n)]for _ in range(m)]
        return helper(startRow, startColumn, maxMove, dp)

            
