class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        i = 1  # Position to overwrite next unique element
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 1]:  # Check for the second occurrence
                i += 1
                nums[i] = nums[j]

        return i + 1
