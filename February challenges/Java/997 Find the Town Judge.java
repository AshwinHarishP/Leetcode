class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] Indegree = new int[n+1];
        int[] Outdegree = new int[n+1];

        for(int[] relation: trust){
            int u = relation[0];
            int v = relation[1];
            Outdegree[u] += 1;
            Indegree[v] += 1;
        }
        for(int i = 1; i <= n; i++){
            if(Outdegree[i] == 0 && Indegree[i] == n-1){
                return i;
            }
        }
        return -1;
    }
}
