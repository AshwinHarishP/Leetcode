class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [""]

        group = dict()

        for i in strs:
            sorted_ele = "".join(sorted(i))

            if sorted_ele in group:
                group[sorted_ele].append(i)
            else:
                group[sorted_ele] = [i]
        return group.values()
