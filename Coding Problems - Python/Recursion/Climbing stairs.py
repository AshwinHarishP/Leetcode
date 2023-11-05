class Solution:
    def climbStairs(self, n: int) -> int:
        temp = 0
        memo = dict()

        def count_steps(temp):
            if temp in memo:
                return memo[temp]

            if temp > n:
                return 0
            if temp == n:
                temp = 0
                return 1

            res = count_steps(temp + 1) + count_steps(temp + 2)
            memo[temp] = res
            return res

        return count_steps(temp)
