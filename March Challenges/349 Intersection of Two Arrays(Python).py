class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_s = set(nums1)
        nums2_s = set(nums2)

        return list(nums1_s.intersection(nums2_s))
