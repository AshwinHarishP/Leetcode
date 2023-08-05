class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_num = []
        for i in nums:
            if i != val:
                new_num.append(i)
        nums[:] = new_num

        return len(nums)
