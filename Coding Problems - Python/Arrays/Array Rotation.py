class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rotate = k % len(nums)
        nums[:] = nums[-rotate :] + nums[:-rotate]
        return nums
