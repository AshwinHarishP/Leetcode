class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1

        def helper(nums, target, start, end):

            if start > end:
                return -1

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                return helper(nums, target, mid+1, end)

            return helper(nums, target, start, mid-1)

        return helper(nums, target, start, end)
