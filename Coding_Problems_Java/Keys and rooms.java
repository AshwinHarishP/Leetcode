class Solution {
    private void dfs(int node, int[] visited, List<List<Integer>> rooms){
        visited[node] = 1;
        List<Integer> adj_room = rooms.get(node);

        for(int room: adj_room){
            if(visited[room]==0){
                dfs(room, visited, rooms);
            }
        }
    }
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        int [] visited = new int[n];

        dfs(0, visited, rooms);
        for(int i = 0; i < n; i++){
            if (visited[i] == 0){
                return false;
            }
        }
        return true;
    }
    
}
