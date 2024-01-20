class Solution:
    def calculate_res(self, k, x):
        complete = k // (2 ** x)
        ans1 = (2 ** (x - 1)) * complete
        remainder = k % (2 ** x)
        ans1 += max(0, remainder - (2 ** (x - 1)))
        return ans1

    def check(self, mid, x, k):
        ans = 0
        for bit in range(x, int(mid.bit_length()) + 2, x):
            ans += self.calculate_res(mid + 1, bit)
        return ans <= k

    def findMaximumNumber(self, k, x):
        l = 1
        r = 10**15
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if self.check(mid, x, k):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans




