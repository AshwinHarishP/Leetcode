class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        res = ""

        res = [i[::-1] for i in s]
        return " ".join(res)
