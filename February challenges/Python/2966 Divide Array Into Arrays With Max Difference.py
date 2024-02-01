class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        i = 0

        while i < n:
            new_nums = nums[i:i+3]    
            if abs(new_nums[0] - new_nums[-1]) <= k:
                res.append(new_nums)
            else:
                res.clear()
                break
            i += 3
    
        return res
