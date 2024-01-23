class Solution {
    public int[] findErrorNums(int[] nums) {
        int i = 0;
        while(i < nums.length){
            int crt = nums[i]-1;
            if(nums[i] != nums[crt]){
                int temp = nums[i];
                nums[i] = nums[crt];
                nums[crt] = temp;
            }
            else{
                i += 1;
            }
        }
        for(int j = 0; j < nums.length; j++){
            if (nums[j] != j+1){
                return new int[]{nums[j], j+1};
            }
        }
        return new int[]{};
    }
}
