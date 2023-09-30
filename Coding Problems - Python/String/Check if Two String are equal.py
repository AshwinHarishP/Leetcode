class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        s2 = "".join(word2)
        s1 = "".join(word1)
        return s1 == s2
        
