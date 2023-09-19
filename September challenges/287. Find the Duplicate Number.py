class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict_ele = {}

        for i in range(len(nums)):
            if nums[i] not in dict_ele.keys():
                dict_ele[nums[i]] = i
            else:
                return nums[i]
        
