class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int n = graph.length;
        List<List<Integer>> res = new ArrayList<>();
        ArrayList<Integer> path = new ArrayList<>();

        dfs(0, graph, path, res, n);
        return res;
    }
    private void dfs(int node, int[][] graph, List<Integer> path, List<List<Integer>> res, int n){
    
        if(node == n-1){
            path.add(node);
            res.add(new ArrayList<>(path));
            path.remove(path.size()-1);
            return;
        }
        path.add(node);
        for(int adjNode: graph[node]){
            dfs(adjNode, graph, path, res, n);
        }
        path.remove(path.size()-1);
    }
}
