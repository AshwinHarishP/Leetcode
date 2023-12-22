class Solution:
    def maxScore(self, s: str) -> int:
        left, maxi, right = 0, 0, s.count("1")

        for i in range(len(s)-1):
            left += s[i] == "0"
            right -= s[i] == "1"
            maxi = max(maxi, left + right)

        return maxi
