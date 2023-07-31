from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_val = Counter(arr)
        count_list = []

        for key, value in count_val.items():
            count_list.append(value)

        set_count_list = list(set(count_list))

        return len(count_list) == len(set_count_list)
            

        
