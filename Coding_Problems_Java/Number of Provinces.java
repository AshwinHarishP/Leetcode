class Solution {
    private void dfs(int node, int[][] adjLs, int[] visited){
        visited[node] = 1;
        for(int i : adjLs[node]){
            if(visited[i] == 0){
                dfs(i, adjLs, visited);
            }
        }
    }
    
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        int[][] adjLs = new int[n][n];
        int [] visited = new int[n];
        int cnt = 0;

        for(int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if(i != j && isConnected[i][j] == 1){
                    adjLs[i][j] = j;
                    adjLs[j][j] = i;
                }
            }
        }
        for(int i = 0; i < n; i++){
            if (visited[i] == 0){
                cnt += 1;
                dfs(i, adjLs, visited);
            }
        }
        return cnt;
    }
}
