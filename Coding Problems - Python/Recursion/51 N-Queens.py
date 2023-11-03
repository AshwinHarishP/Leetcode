class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def n_queen(board, r):
            if r == n:
                display(board)
                return 

            for c in range(n):
                if is_safe(board, r, c):
                    board[r][c] = True
                    n_queen(board, r + 1)
                    board[r][c] = False

        def is_safe(board, r, c):
            # Check upward
            for i in range(r):
                if board[i][c]:
                    return False

            # Check left diagonal
            for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
                if board[i][j]:
                    return False

            # Check right diagonal
            for i, j in zip(range(r, -1, -1), range(c, n)):
                if board[i][j]:
                    return False

            return True

        def display(board):
            solution = []
            for i in range(n):
                row = ""
                for j in range(n):
                    if board[i][j]:
                        row += "Q"
                    else:
                        row += "."
                solution.append(row)
            res.append(solution)

        res = []
        board = [[False for _ in range(n)] for _ in range(n)]
        n_queen(board, 0)
        return res
