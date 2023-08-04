class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # Case 1:
        if len(p) > len(s): 
            return []
        # Case 2:
        dict_s, dict_p = {}, {}
    
        # Adding p elements in hashmap 
        for i in range(len(p)):
            dict_p[p[i]] = 1 + dict_p.get(p[i], 0)
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
        
        # if both hash are same appending index 0
        if dict_s == dict_p:
            res = [0]
        else:
            res = []
    
        l = 0
        for r in range(len(p),len(s)):
        
        # Adding right pointer element and removing left pointer element in hashmap
            dict_s[s[r]] = 1 + dict_s.get(s[r], 0)
            dict_s[s[l]] -= 1
    
        # If hashmap left pointer has empty element, remove element
            if dict_s[s[l]] == 0:
                dict_s.pop(s[l])
        
            l += 1
        
        # Check both hashes are same         
            if dict_s == dict_p:
                res.append(l)
        
        return res
