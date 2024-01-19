import java.util.Arrays;

class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        int mini = Integer.MAX_VALUE;
        
        for (int i = 0; i < m; i++) {
            int res = func(matrix, 0, i, n, m);
            mini = Math.min(mini, res);
        }
        return mini;
    }

    public int func(int[][] matrix, int r, int c, int n, int m) {
        int[] prev = new int[m + 1];
        Arrays.fill(prev, Integer.MAX_VALUE);

        for (int j = 0; j < m; j++) {
            prev[j] = matrix[n - 1][j];
        }

        for (int i = n - 2; i >= 0; i--) {
            int[] curr = new int[m + 1];
            Arrays.fill(curr, Integer.MAX_VALUE);

            for (int j = m - 1; j >= 0; j--) {
                int ld = Integer.MAX_VALUE, rd = Integer.MAX_VALUE, below = Integer.MAX_VALUE;
                
                if (i + 1 < n && j - 1 >= 0) {
                    ld = matrix[i][j] + prev[j - 1];
                }
                if (i + 1 < n && j + 1 < m) {
                    rd = matrix[i][j] + prev[j + 1];
                }
                if (i + 1 < n) {
                    below = matrix[i][j] + prev[j];
                }

                curr[j] = Math.min(Math.min(ld, rd), below);
            }

            System.arraycopy(curr, 0, prev, 0, curr.length);
        }
        return prev[c];
    }
}
