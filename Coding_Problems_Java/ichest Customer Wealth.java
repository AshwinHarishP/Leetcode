class Solution {
    public int maximumWealth(int[][] accounts) {
        int max_ele = Integer.MIN_VALUE;

        for(int i = 0; i < accounts.length; i++){
            int sum = 0;
            for (int j = 0; j < accounts[i].length; j++){
                sum += accounts[i][j];
            }

            max_ele = Math.max(max_ele, sum);
        }
        return max_ele;
    }
}
