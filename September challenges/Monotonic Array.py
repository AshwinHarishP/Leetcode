class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reverse = sorted(nums,reverse = True)
        sort = sorted(nums)

        if sort == nums or reverse == nums:
            return True
        return False
