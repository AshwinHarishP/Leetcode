class Solution {
    public int rob(int[] nums) {
        int[] prev = new int[nums.length];
        prev[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int[] curr = new int[nums.length];

            int take = nums[i] + (i - 2 >= 0 ? prev[i - 2] : 0);
            int not_take = prev[i - 1];

            curr[i] = Math.max(take, not_take);
            prev[i] = curr[i];
        }

        return prev[nums.length - 1];
    }
}
