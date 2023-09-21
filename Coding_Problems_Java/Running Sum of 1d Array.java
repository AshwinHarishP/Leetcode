class Solution {
    public int[] runningSum(int[] nums) {
        int sum = 0;
        int [] sum_res = new int[nums.length];

        for (int i = 0; i < nums.length; i++){
            sum += nums[i];
            sum_res[i] = sum;
        }

        return sum_res;
    }
}
