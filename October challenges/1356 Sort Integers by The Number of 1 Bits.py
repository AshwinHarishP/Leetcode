class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        sorted_list = sorted(arr, key = lambda x: (x.bit_count(), x))
        return sorted_list
        
