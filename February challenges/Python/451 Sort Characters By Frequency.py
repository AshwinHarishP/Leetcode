from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        new_s = ""
        count = Counter(s)
        ls = []
        for key, value in count.items():
            ls.append([key, value])
        ls = sorted(ls, key=lambda x: x[1], reverse= True)

        for i in ls:
            new_s += i[0] * i[1]
        return new_s
