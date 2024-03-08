class Solution {
    public int maxFrequencyElements(int[] nums) {
        int[] values = new int[101];
        for(int i= 0; i < nums.length; i++){
            values[nums[i]] += 1;
        }
        ArrayList<Integer> ls = new ArrayList<>();
        for (int i: values) ls.add(i);
        int max_val = Integer.MIN_VALUE;
        int res = 0;

        for(int i = 0; i < ls.size(); i++){
            if(ls.get(i) > max_val){
                max_val = ls.get(i);
            }
        }
        for(int i: ls){
            if (i == max_val) res += i;
        }
        return res;
        
    }
}
