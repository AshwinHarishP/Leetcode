class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        dict_ele = dict(zip(letters,code))
        count = 0
        old = ""
        transformations = set()
        for i in range(len(words)):
            transform = ""
            for j in range(len(words[i])):
                transform += dict_ele[words[i][j]]

            transformations.add(transform)
            
        return len(transformations)
