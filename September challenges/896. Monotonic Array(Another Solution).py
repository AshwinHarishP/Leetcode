class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        for i in range(len(nums)-2):
            if (nums[i] >= nums[i+1] >= nums[i+2]) or (nums[i] <= nums[i+1] <= nums[i+2]):
                return True
        return False
        
