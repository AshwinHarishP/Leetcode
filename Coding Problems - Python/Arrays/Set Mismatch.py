class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        ls = []
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct],nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                ls.append(nums[i])
                ls.append(i+1)

        return ls
