class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        res = ""

        for i in s:
            res += i[::-1] +" "
        return res.strip(" ")
