class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed = sorted(allowed)
        words = sorted(words)
        words_list = []
        count = 0

        for i in range(len(words)):
            tmp_list = []
            for j in range(len(words[i])):
                tmp_list.append(words[i][j])
            words_list.append(tmp_list)
        

        for i in range(len(words_list)):
            for j in range(len(words_list[i])):
                if words_list[i][j] not in allowed:
                    print(words[i])
                    count += 1
                    break
        return len(words) - count
        

