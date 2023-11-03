class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col, count = len(grid), len(grid[0]), 0
        def helper(grid, r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != "1":
                return False

            grid[r][c] = 2

            res = (helper(grid, r + 1, c) or 
                   helper(grid, r - 1, c) or 
                   helper(grid, r, c + 1) or 
                   helper(grid, r, c - 1))

        for i in range(row):
            for j in range(col):
                if grid[i][j] =="1":
                    count += 1
                helper(grid, i, j)

        return count




    
