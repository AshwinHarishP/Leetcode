class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] conactenated_array = new int[2*nums.length];

        System.arraycopy(nums, 0, conactenated_array,0,nums.length);
        System.arraycopy(nums, 0, conactenated_array,nums.length,nums.length);

        return conactenated_array;

    }
}
