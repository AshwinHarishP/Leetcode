class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        index = -1
        length = len(nums)
        n = 0
        numbers = {}

        for num in nums:
            x -= num
        if x == 0:
            return length

        for i in range(len(nums)):
            n += nums[i]
            if n == -x:
                index = i + 1
            if n not in numbers:
                numbers[n] = i
            if n+x in numbers:
                index = max(index, i - numbers[n+x])

        return length - index if index != -1 else index
