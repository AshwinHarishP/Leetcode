class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < nums.length; i++){
            arr.add(index[i], nums[i]);
        }
        int [] res_arr = new int[arr.size()];

        for (int i = 0; i < arr.size(); i++){
            res_arr[i] = arr.get(i);
        }
        return res_arr;
    }
}
