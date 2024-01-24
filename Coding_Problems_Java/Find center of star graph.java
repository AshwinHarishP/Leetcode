class Solution {
    public int findCenter(int[][] edges) {
        int n = edges.length;
        HashMap<Integer,Integer> hm = new HashMap<>();

        for(int[] edge: edges){
            int u = edge[0];
            int v = edge[1];

            hm.put(u, hm.getOrDefault(u, 0)+1);
            hm.put(v, hm.getOrDefault(v, 0)+1);
        }
        for (Map.Entry<Integer, Integer> entry : hm.entrySet()){
            if(entry.getValue() == n){
                return entry.getKey();
            }
        }
        return -1;
    }
}
