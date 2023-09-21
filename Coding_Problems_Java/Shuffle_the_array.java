class Solution {
    public int[] shuffle(int[] nums, int n) {
        ArrayList<Integer> res = new ArrayList<>();
        ArrayList<Integer> nums1 = new ArrayList<>();
        ArrayList<Integer> nums2 = new ArrayList<>();

        for (int i = 0; i < n; i++){
            nums1.add(nums[i]);
        }

        for (int i = n; i < nums.length; i++){
            nums2.add(nums[i]);
        }

        
        for (int i = 0; i < nums1.size(); i++){
            res.add(nums1.get(i));
            res.add(nums2.get(i));
        }

        int [] res_arr = new int[res.size()];

        for (int i = 0; i < res.size(); i++){
            res_arr[i] = res.get(i);
        }

        return res_arr;
        
    }
}
