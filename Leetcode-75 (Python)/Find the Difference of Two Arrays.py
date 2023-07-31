class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        nums1_diff = list(nums1 - nums2)
        nums2_diff = list(nums2 - nums1)
        
        return [nums1_diff, nums2_diff]
