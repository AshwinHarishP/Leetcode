class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i, num in enumerate(nums):
                if target < num:
                    return i

            return len(nums)
