class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        tmp = ""
        for i in range(len(words)):
            tmp += words[i][0]

        return tmp == s
        
