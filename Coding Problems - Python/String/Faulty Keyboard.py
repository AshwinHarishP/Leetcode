class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""

        for i in s:
            if i == "i":
                res = res[::-1]
            else:
                res += i

        return res
