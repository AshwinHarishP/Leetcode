class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            index = nums[i]
            result.append(nums[index])
        return result
