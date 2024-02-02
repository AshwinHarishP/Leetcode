class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        int[] Indegree = new int[n];
        ArrayList<Integer> res = new ArrayList<>();

        for(List<Integer> i: edges){
            int u = i.get(0);
            int v = i.get(1);
            Indegree[v] += 1;
        }
        for (int i = 0;i < n; i++){
            if (Indegree[i] == 0){
                res.add(i);
            }
        }
        return res;
    }
}
