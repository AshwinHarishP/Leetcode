class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper():
            prev = [0 for _ in range(len(nums))]
            prev[0] = nums[0]

            for i in range(1, len(nums)):
                curr = [0 for _ in range(len(nums))]

                take = nums[i] + prev[i-2]
                not_take = 0 + prev[i-1]

                curr[i] = max(take, not_take)
                
                prev[i] = curr[i]
            return prev[len(nums)-1]

        return helper()
        
