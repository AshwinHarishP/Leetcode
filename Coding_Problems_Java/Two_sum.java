class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hmap = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int K = target - nums[i];

            if (hmap.containsKey(K)){
                return new int []{hmap.get(K), i};
            }
            else{
                hmap.put(nums[i],i);
            }
        }
        return new int []{};   
    }
}
