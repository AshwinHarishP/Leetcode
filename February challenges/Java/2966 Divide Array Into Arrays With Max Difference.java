class Solution {
    public int[][] divideArray(int[] nums, int k) {
        int n = nums.length;
        int i = 0;
        Arrays.sort(nums);
        ArrayList<int[]> res = new ArrayList<>();
        while(i < n){
            int[] subarray = {nums[i], nums[i+1], nums[i+2]};

            if(Math.abs(subarray[0] - subarray[2]) <= k){
                res.add(subarray);
            }
            else{
                res.clear();
                break;
            }
            i += 3;
        }
        return res.toArray(new int[res.size()][]);
        
    }
}
