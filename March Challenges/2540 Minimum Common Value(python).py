class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        res = list(nums1_set.intersection(nums2_set))
        if not res:
            return -1
        return min(res)
