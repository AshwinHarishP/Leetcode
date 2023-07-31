class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_list = []
        for i in nums:
            if i != 0:
                new_list.append(i)

        count_zero = nums.count(0)

        for j in range(count_zero):
            new_list.append(0)

        nums[:] = new_list
