class Solution {
    public int numIdenticalPairs(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++){
            int j = i + 1;

            while(j < nums.length){
                if (nums[i] == nums[j]){
                    count += 1;
                }
                j += 1;
            }
        }

        return count;
    }
}
