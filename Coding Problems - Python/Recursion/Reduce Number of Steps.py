class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        def helper(num, count):
            # Base Case
            if num == 0:
                return count

            if num % 2 == 0:
                return helper(num//2, count+1)
            return helper(num-1, count+1)

        return helper(num, count)
