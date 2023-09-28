class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, lc, rc = 0, 0, 0
        for i in range(len(s)):
            if lc == rc:
                count += 1
                lc = 0
                rc = 0
            if s[i] == "L":
                lc += 1
            else:
                rc += 1
        return count
