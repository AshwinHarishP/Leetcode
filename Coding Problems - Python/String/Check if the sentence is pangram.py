class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s = "abcdefghijklmnopqrstuvwxyz"
        sentence = "".join(sorted(list(set(sentence))))
        print(sentence)
        return sentence == s
        
