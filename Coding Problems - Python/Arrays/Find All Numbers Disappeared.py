class Solution:
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        i = 0
        ls = []
        while i < len(arr):
            c = arr[i]-1
            if arr[i] != arr[c]:
                arr[i], arr[c] = arr[c], arr[i]
            else:
                i += 1


        for i in range(len(arr)):
            if i+1 != arr[i]:
                ls.append(i+1)

        return ls
