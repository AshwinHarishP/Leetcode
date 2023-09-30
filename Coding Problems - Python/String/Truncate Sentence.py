class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.split(" ")
        new_s = ""

        for i in range(k):
            new_s += s[i] +" "
        return new_s.strip(" ")
        
