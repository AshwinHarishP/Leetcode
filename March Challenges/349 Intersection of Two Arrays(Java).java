class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> nums1_s = new HashSet<>();
        HashSet<Integer> nums2_s = new HashSet<>();

        for(int i: nums1) nums1_s.add(i);
        for(int i: nums2) nums2_s.add(i);

        HashSet<Integer>temp = new HashSet<>(nums1_s);
        temp.retainAll(nums2_s);

        List<Integer> temp1 = new ArrayList<>(temp);
        int[] res = temp1.stream().mapToInt(Integer::intValue).toArray();
        return res;
    }
}
