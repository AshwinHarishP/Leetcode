class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum = 0
        max_sum = int(nums[0])

        for i in nums:
            
            if Sum < 0:
                Sum = 0

            Sum += i
            max_sum = max([max_sum, Sum])
        return max_sum
        
