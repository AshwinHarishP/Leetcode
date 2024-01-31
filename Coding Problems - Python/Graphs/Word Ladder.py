from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        Q = deque()
        Q.append([beginWord, 1])
        wordList = set(wordList)
        wordList.discard(beginWord)

        while Q:
            word, step = Q.popleft()
            if word == endWord:
                return step
            
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in wordList:
                        Q.append([new_word, step+1])
                        wordList.remove(new_word)
        return 0
                    

        
