import java.util.*;

class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        Set<Integer> nums1Set = new HashSet<>();
        Set<Integer> nums2Set = new HashSet<>();
        
        for (int num : nums1) {
            nums1Set.add(num);
        }
        
        for (int num : nums2) {
            nums2Set.add(num);
        }
        
        nums1Set.retainAll(nums2Set);

        if (nums1Set.isEmpty()) {
            return -1;
        }
        
        int minCommon = Integer.MAX_VALUE;
        for (int num : nums1Set) {
            if (num < minCommon){
                minCommon = num;
            }
        }
        
        return minCommon;
    }
}
