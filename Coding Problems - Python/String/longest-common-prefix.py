class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs = sorted(strs)     # Sort the List 
        last = len(strs) - 1    # Last element
        
        
        # Finding minimum
        minimum = len(strs[0])
        for i in strs:
            if len(i) < minimum:
                minimum = len(i)
        
        # Checking first element first character and last element first character
        prefix = ""
        for i in range(minimum):
            if strs[0][i] == strs[last][i]:
                prefix += strs[0][i]
            else:
                break
       
        return prefix

        
